from tkinter import *
from tkinter import ttk
# from Pub_extraction_code_and_other_things.SearchItem import SearchItem
from data_storage import Publication
import scholarly
from Pub_extraction_code_and_other_things.PubItem import PubItem
from data_storage import data_list as dl

class SearchBar:

    def __init__(self, mainframe):
        search = StringVar()

        search_frame = ttk.Frame(mainframe, padding="3 3 12 12")
        search_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        search_frame.columnconfigure(1, weight=1)

        #search_frame.rowconfigure(0, weight=1)

        ttk.Label(search_frame, text="Google Scholar Search: ").grid(column=0, row=0, sticky=(N, E, S, W))
        search_entry = ttk.Entry(search_frame, textvariable=search)
        search_entry.grid(column=1, row=0, sticky=(N, W, E, S))

        def search_gs(*args):
            if search.get() == "":
                pass
            else:
                try:
                    search_window = Toplevel()
                    search_window.title('Search results')
                    mainframe = ttk.Frame(search_window, padding="3 3 12 12")
                    mainframe.grid(column=0, row=0, sticky="")
                    mainframe.columnconfigure(0, weight=1)

                    ttk.Label(mainframe, text="First 10 results").grid(column=0, row=0, sticky="")
                    pub_list_frame = ttk.Frame(mainframe, padding="3 3 12 12")
                    pub_list_frame.grid(column=0, row=1, sticky=(N, W, E, S))
                    pub_list_frame.columnconfigure(1, weight=1)

                    search_query = scholarly.search_pubs_query(search.get())

                    #list 10 results
                    for i in range(10):
                        SearchItem(search_query, pub_list_frame, i)

                except ValueError:
                    pass

        ttk.Button(search_frame, text="Submit", command=search_gs).grid(column=2, row=0, sticky=(N, W, S, E))
        search_entry.bind('<Return>', search_gs)

class SearchItem:

    def __init__(self, search_query, pub_list_frame, position):
        pub = next(search_query)
        pub_list_item = ttk.Frame(pub_list_frame, padding="3 3 12 12")
        pub_list_item.grid(column=0, row=position, sticky=(N, W, E, S))
        pub_list_item.columnconfigure(1, weight=1)
        ttk.Separator(pub_list_item).grid(column=0, columnspan=3, row=0, sticky=(E, W))

        list_number = ttk.Label(pub_list_item, text=str(position + 1))
        list_number.grid(column=0, row=1, sticky=(N, W, E, S))

        title = ttk.Label(pub_list_item, text=pub.bib['title'].strip(), font=("Segoe UI", 9, "bold"))
        title.grid(column=1, row=1, sticky=(N, W, E, S))
        info = ttk.Label(pub_list_item, text='Authors: ' + ', '.join(pub.bib['author'].split(' and ')))
        info.grid(column=1, row=2, sticky=(N, W, E, S))

        def add_to_library():
            # from GUI import lib_pub_list_frame
            add_button["text"] = "Added"
            new_pub = Publication()
            new_pub.set_data(pub.bib['title'].strip(), 'C:\\Users\\Lin\\Desktop\\history.txt', 'search')
            # pl_item = PubItem(new_pub, lib_pub_list_frame, len(dl))

        add_button = ttk.Button(pub_list_item, text="Add", command=add_to_library)
        add_button.grid(column=2, row=2, sticky=(N, E, S))
