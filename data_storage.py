# import csv
import json
from Pub_extraction_code_and_other_things import pubextraction as pe
import extract_metadata as em
import datetime
from fuzzywuzzy import fuzz
from Pub_extraction_code_and_other_things import get_references as gr


DUPLICATE = "duplicate"
NEW = "new"


data_path = 'data.json'

data_list = []
try:
    with open(data_path) as data:
        data_list = json.load(data)
except FileNotFoundError:
    data_list = []

class Publication:
    def __init__(self):
        self.id = None
        self.title = None
        self.year = None
        self.authors = None
        self.journal = None
        self.gscholar_link = None

        # If the file_path is null, then the paper is not in the library
        self.file_path = None
        self.references = None
        self.source = None
        self.tags = None
        self.notes = None
        self.quotes = None
        self.date_retrieved = str(datetime.datetime.now())
        self.status = "Unknown"
        self.printed = None
        # self.info = None

    def set_data(self, title, file, source=''):
        pubext = pe.retrieve_publications_scholar_py(title)[0]
        schly = em.scholarly_extract(title)
        self.title = pubext['title']
        self.year = pubext['year']
        self.authors = schly.bib['author'].split(' and ')
        self.gscholar_link = schly.url_scholarbib
        self.references = gr.get_references(title)
        if source == 'search':
            self.source = 'Keyword search'
        if source == 'backward':
            self.source = 'Backward citation'
        if source == 'forward':
            self.source = 'Forward citation'
        t = match_paper(self)
        # skip match_paper
        t = NEW
        if t == NEW:
            data_list.append(self.__dict__)
            self.id = len(data_list) - 1
        # data_list.append(self.__dict__)
        record_history(self, file, t)


def store_data():
    # with open(csv_file, 'a', newline = '') as file:
        # writer = csv.writer(file)
        # writer.writerows([self.info])
    with open(data_path, 'w') as outfile:
        json.dump(data_list, outfile, indent = 4)
    outfile.close()


def record_history(pub, file, t):
    with open(file, 'a') as file:
        if t == NEW:
            file.write('Added "' + pub.title + '" to the library (' + pub.date_retrieved + ')')
        elif t == DUPLICATE:
            file.write('"' + pub.title + '" is a duplicate (' + pub.date_retrieved + ')')
    file.close()


def match_paper(pub):
    for paper in data_list:
        if fuzz.ratio(pub.title, paper['title']) > 90:
            numauthors = len(pub.authors)
            if numauthors == paper['authors']:
                for author in range(numauthors):
                    if not any(fuzz.token_sort_ratio(pub.authors[author], paper['authors'][i]) for i in range(numauthors)) > 80:
                        return DUPLICATE
                return NEW
            else:
                return DUPLICATE
        else:
            return DUPLICATE


if __name__ == "__main__":
    # pub = Publication()
    # pub.id = 1
    # pub.title = "Title"
    # pub.year = 2016
    # pub.authors = ["Smith, John", "Doe, Jane"]
    # pub.journal = "Journal"
    # pub.gscholar_link = "http://123.com"
    # pub.file_path = "file->path"
    # pub.references = ["Title2", "Title3"]
    # pub.source = "source"
    # pub.tags = ["tag1", "tag2"]
    # pub.notes = ["A note."]
    # pub.quotes = ["A quote.", "Another quote."]
    # pub.date_retrieved = "October 6, 2016", "to be read"
    # # pub.info = [pub.id, pub.title, pub.year, pub.authors, pub.journal,
    #                  # pub.gscholar_link, pub.file_path, pub.references,
    #                  # pub.user_keywords, pub.source, pub.tags, pub.notes,
    #                  # pub.quotes, pub.date_retrieved, pub.status]
    # # pub.store_paper('C:\\Users\\Lin\\Desktop\\csv1.csv')
    # pub1.info = [pub1.id, pub1.title, pub1.year, pub1.authors, pub1.journal,
                     # pub1.gscholar_link, pub1.file_path, pub1.references,
                     # pub1.user_keywords, pub1.source, pub1.tags, pub1.notes,
                     # pub1.quotes, pub1.date_retrieved, pub1.status]
    # pub1.store_paper('C:\\Users\\Lin\\Desktop\\csv1.csv')
    pub1 = Publication()
    pub1.set_data("Reference management software: a comparative analysis of four products", 'history.txt')
    pub2 = Publication()
    pub2.set_data("Reference management software: a comparative analysis of four products", 'history.txt')
    store_data()
