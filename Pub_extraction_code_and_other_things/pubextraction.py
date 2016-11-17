__author__ = 'nicole'

import subprocess

import scholarly

from Pub_extraction_code_and_other_things import scholar


def extract_bib(pdf_file):
    return _extract("pdf-extract extract-bib \"%s\"" % pdf_file)


def extract_refs(pdf_file):
    return _extract("pdf-extract extract --references \'%s\'" % pdf_file)

def extract_title(pdf_file):
    _extract("cd C:\\Ruby22-x64\\bin\\ruby")
    return _extract("pdf-extract extract --references \'%s\'" % pdf_file)

def _extract(command):
    #return os.system(command)

    p=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, errors = p.communicate()
    return output

# def docear_extract_title(pdf_file):
#     command = "java -jar external/docears-pdf-inspector.jar -title \"%s\"" % pdf_file
#     return unicode(_extract(command).strip(),"utf-8",errors='ignore')

def grobid_extract(path):
    exes = ['processFullText','processHeader','processReferences']

    grobid_path = '~/Documents/dev/libs/grobid-master/grobid-core/target/grobid-core-0.4.1-SNAPSHOT.one-jar.jar'
    grobid_home = '~/Documents/dev/libs/grobid-master/grobid-home'
    grobid_props = '~/Documents/dev/libs/grobid-master/grobid-home/config/grobid.properties'
    grobid_input = path
    grobid_output = "~/Documents/dev/PyCharmProjects/refManager/temp"
    exe = exes[0]
    command = "java -Xmx1024m -jar %s -gH %s -gP %s -dIn %s -dOut %s -exe %s" % (grobid_path,
                                                                                 grobid_home,
                                                                                 grobid_props,
                                                                                 grobid_input,
                                                                                 grobid_output,
                                                                                 exe)
    print(command)
    #return _extract(command)

def retrieve_publications_scholar_py(pubname):
    querier = scholar.ScholarQuerier()
    settings = scholar.ScholarSettings()
    #settings.set_citation_format(scholar.ScholarSettings.CITFORM_BIBTEX)
    querier.apply_settings(settings)
    query = scholar.SearchScholarQuery()
    query.set_phrase(pubname)
    #query.set_words(options.allw)
    query.set_include_patents(False)
    query.set_num_page_results(1)
    querier.send_query(query)
    #scholar.csv(querier, header=True) #prints as csv
    ret = []
    for a in querier.articles:
        pa = {'year':a.attrs['year'][0],
              'citations':a.attrs['num_citations'][0],
              'title':a.attrs['title'][0],
              'url':a.attrs['url'][0],
              'excerpt':a.attrs['excerpt'][0]
              }
        ret.append(pa)
    return ret


def retrieve_publication_scholarly(pubname):
    search_query = scholarly.search_pubs_query(pubname)
    return (next(search_query))

#Secret Mendeley
#bYBfgZPiXqHT7hnp

# def mendeley_extract(file):
#     mend = Mendeley('nicksultanum@gmail.com',client_secret='bYBfgZPiXqHT7hnp')
#     auth = mend.start_client_credentials_flow()
#     session = auth.authenticate()
#
#     #https://mendeleyapi.wordpress.com/tag/metadata-extraction-tools/
#     ret = session.documents.create_from_file(file)
#     return ret

def main():
    #grobid_extract('/Users/nicole/OneDrive/Library/_TO_READ/gestures')
    #pubname = "Has general practitioner computing made a difference to patient care? A systematic review of published reports"
    pubname = "Reference management software: a comparative analysis of four products"
    #print retrieve_publication_scholarly(pubname)
    print(retrieve_publications_scholar_py(pubname))
    #print(extract_refs('C:\\Users\\Lin\\Desktop\\CSC494\\Reference Management\\(2016) Citerivers.pdf'))
    #print(extract_title('C:\\Users\\Lin\\Desktop\\CSC494\\Reference Management\\(2016) Citerivers.pdf'))



if __name__ == "__main__":
    main()
