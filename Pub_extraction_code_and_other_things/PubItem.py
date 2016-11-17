from tkinter import *
from tkinter import ttk
import ast


class PubItem:

    def __init__(self, pub, pub_list_frame, position):

        pub_list_item = ttk.Frame(pub_list_frame, padding="3 3 12 12")
        pub_list_item.grid(column=0, row=position, sticky=(N, W, E, S))
        pub_list_item.columnconfigure(1, weight=1)
        ttk.Separator(pub_list_item).grid(column=0, columnspan=3, row=0, sticky=(E, W))

        list_number = ttk.Label(pub_list_item, text=str(position + 1))
        list_number.grid(column=0, row=1, sticky=(N, W, E, S))

        title = ttk.Label(pub_list_item, text=pub['title'], font=("Segoe UI", 9, "bold"))
        title.grid(column=1, row=1, sticky=(N, W, E, S))
        info = ttk.Label(pub_list_item, text='Authors: ' + ', '.join(pub['authors']) + '\nDate Retrieved: ' + pub['date_retrieved'].split()[0])
        info.grid(column=1, row=2, sticky=(N, W, E, S))

        status_frame = ttk.Frame(pub_list_item)
        status_frame.grid(column=2, row=1, rowspan=2, sticky=(N, W, E, S))
        status_label = ttk.Label(status_frame, text='Status: ')
        status_label.grid(column=0, row=0, sticky=(N, W, E, S))
        statusvar = StringVar(status_frame)
        statusvar.set(pub['status']) # default value

        def change_status(*args):
            pub['status'] = statusvar.get()
            print(pub['status'])

        status = OptionMenu(status_frame, statusvar, "Unknown", "To be read", "Read", "Relevant", "Irrelevant", command=change_status)
        status.config(width=10)
        status.grid(column=1, row=0, sticky=(N, E, S))

        def open_edit(*args):
            edit_window = Toplevel()
            edit_window.title("Edit")
            mainframe = ttk.Frame(edit_window, padding="3 3 12 12")
            mainframe.grid(column=0, row=0, sticky="")
            mainframe.columnconfigure(0, weight=1)
            mainframe.rowconfigure(0, weight=1)

            ttk.Label(mainframe, text='Editing ' + '"' + pub['title'] + '"').grid(column=0, row=1, sticky=(N, W, E, S))

        #     self.title = None
        #     self.year = None
        # self.authors = None
        # self.journal = None
        # self.gscholar_link = None
        #
        # # If the file_path is null, then the paper is not in the library
        # self.file_path = None
        # self.references = None
        # self.source = None
        # self.tags = None
        # self.notes = None
        # self.quotes = None
        # self.date_retrieved = str(datetime.datetime.now())
        # self.status = "Unknown"
        # self.printed = None

            edit_title = EditEntry(pub, mainframe, "Title", 2)
            edit_authors = EditEntry(pub, mainframe, "Authors", 3)
            edit_journal = EditEntry(pub, mainframe, "Journal", 4)
            edit_file_path = EditEntry(pub, mainframe, "File path", 5)
            edit_references = EditEntry(pub, mainframe, "References", 6)
            edit_tags = EditEntry(pub, mainframe, "Tags", 7)
            edit_notes = EditEntry(pub, mainframe, "Notes", 8)
            edit_quotes = EditEntry(pub, mainframe, "Quotes", 9)
            edit_printed = EditEntry(pub, mainframe, "Printed", 10)

            def edit_save(*args):
                for field in [edit_title, edit_authors, edit_journal, edit_file_path,
                              edit_references, edit_tags, edit_notes, edit_quotes,
                              edit_printed]:
                    if field == edit_authors or field == edit_references or \
                        field == edit_tags or field == edit_notes or \
                            field == edit_quotes:
                        pub[field.attribute] = ast.literal_eval(field.entry.get())
                    else:
                        pub[field.attribute] = field.entry.get()

            ttk.Button(mainframe, text="Save", command=edit_save).grid(column=0, row=11, sticky=(N, W, E, S))
            mainframe.bind('<Return>', edit_save)

        edit_button = ttk.Button(status_frame, text="Edit", width=10, command=open_edit)
        edit_button.grid(column=1, row=1, sticky=(N, W, E, S))

class EditEntry:

    def __init__(self, pub, mainframe, attribute, position):
        self.entry = StringVar()

        if attribute == "File path":
            self.attribute = 'file_path'
            self.entry.set(pub[self.attribute])

        else:
            self.attribute = attribute.lower()
            self.entry.set(pub[self.attribute])

        edit_frame = ttk.Frame(mainframe, padding="3 3 12 12")
        edit_frame.grid(column=0, row=position, sticky=(N, W, S))
        edit_label = ttk.Label(edit_frame, text=attribute + ":")
        edit_label.grid(column=0, row=0, sticky="E")
        edit_entry = ttk.Entry(edit_frame, width=50, textvariable=self.entry)
        edit_entry.grid(column=1, row=0, sticky=(N, W, S))
