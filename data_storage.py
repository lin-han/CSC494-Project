# import csv
import json
import pubextraction as pe
import extract_metadata as em
import datetime
from fuzzywuzzy import fuzz


DUPLICATE = "duplicate"
NEW = "new"


data_path = 'C:\\Users\\Lin\\Desktop\\data.json'

try:
    data_list = json.load(data_path)
except FileNotFoundError:
    data_list = []

class Publication:
    def __init__(self):
        data_list.append(self)
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
        self.status = None
        self.printed = None
        # self.info = None


    def set_data(self, title, file):
        pubext = pe.retrieve_publications_scholar_py(title)[0]
        schly = em.scholarly_extract(title)
        self.title = pubext['title']
        self.year = pubext['year']
        self.authors = schly.bib['author'].split(' and ')
        self.gscholar_link = schly.url_scholarbib
        t = match_paper(self)
        if t == NEW:
            data_list.append(self)
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
        if fuzz.ratio(pub.title, data_list[paper]['title']) > 90:
            numauthors = pub.authors.length
            if numauthors == data_list[paper]['authors']:
                for author in range(numauthors):
                    if not any(fuzz.token_sort_ratio(pub.authors[author], data_list[paper]['authors'][i]) for i in range(numauthors)) > 80:
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
    pub1.set_data("Reference management software: a comparative analysis of four products")
    pub2 = Publication()
    pub2.set_data("Reference management software: a comparative analysis of four products")
