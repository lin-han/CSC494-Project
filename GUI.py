from tkinter import *
from tkinter import ttk
from data_storage import data_list as dl
from data_storage import store_data as sd
import atexit
from Pub_extraction_code_and_other_things.PubItem import PubItem
from Pub_extraction_code_and_other_things.search import SearchBar
from Pub_extraction_code_and_other_things.AutoScrollbar import AutoScrollbar



root = Tk()


def c_on_resize(event):
        # determine the ratio of old width/height to new width/height
        print(event.widget.winfo_reqwidth())
        # print(event.widget.width)
        wscale = float(event.width)/event.widget.winfo_reqwidth()
        hscale = float(event.height)/event.widget.winfo_reqheight()
        # event.widget.width = event.width
        # event.widget.height = event.height
        # resize the canvas
        # event.widget.config(width=event.width, height=event.height)
        # rescale all the objects tagged with the "all" tag
        event.widget.scale("all",0,0,wscale,hscale)

def on_resize(event):
    # resize the canvas
    event.widget.config(width=event.width, height=event.height)

root.title("Reference Management Tool")
# root.geometry('1000x700')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.pack(fill='both',expand=True)
# mainframe.grid(column=0, row=0, sticky=(N, E, W, S))
mainframe.bind("<Configure>", on_resize)

mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(2, weight=1)

# 1st row
SearchBar(mainframe)

#2nd row
ttk.Label(mainframe, text="Library").grid(column=0, row=1, sticky=(N, S))

#3rd row
pub_scrollbar = Scrollbar(mainframe)
pub_scrollbar.grid(column=1, row=2, sticky=(N, S))

canvas = Canvas(mainframe, yscrollcommand=pub_scrollbar.set, width=800, height=500)
# canvas.pack(fill='both', expand=True)
canvas.grid(column=0, row=2, sticky=(N, E, S, W))
canvas.columnconfigure(0, weight=1)
canvas.config(scrollregion=(0,0,500,500))
canvas.bind("<Configure>", c_on_resize)
pub_scrollbar.config(command=canvas.yview)



pub_list_frame = ttk.Frame(canvas, padding="3 3 12 12")
pub_list_frame.grid(column=0, row=0, sticky=(N, E, S, W))
pub_list_frame.columnconfigure(0, weight=1)

for item in range(len(dl)):
    # pub_list_item = ttk.Label(pub_list_frame, text="item " +
    #                           str(item)).grid(column=0, row=item)
    pub = dl[item]
    pub_list_item = PubItem(pub, pub_list_frame, item)

# canvas.addtag_all("all")

def exit_handler():
    sd()



atexit.register(exit_handler)

canvas.create_window(0, 0, anchor=NW, window=pub_list_frame)
#
pub_list_frame.update_idletasks()
#
# canvas.config(scrollregion=canvas.bbox("all"))

canvas.addtag_all("all")
root.mainloop()
