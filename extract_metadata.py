import pdfx
import scholarly


def extract_metadata(filepath):
    pdf = pdfx.PDFx(filepath)
    # metadata = pdf.get_metadata()
    references = pdf.get_references()
    references_dict = pdf.get_references_as_dict()
    # for result in [metadata, references, references_dict]:
    for reference in references_dict:
        print(references_dict[reference])


def scholarly_extract(title):
    search_query = scholarly.search_pubs_query(title)
    return next(search_query)


if __name__ == "__main__":
    extract_metadata('C:\\Users\\Lin\\Desktop\\CSC494\\Reference Management\\(2016) Citerivers.pdf')

#    extract_metadata('C:\\Users\\Lin\\Desktop\\CSC494\\Reference Management\\(2003) CiteVis- Exploring Conference Paper Citation Data Visually.pdf')
