from tkinter import *
from libraryGenesis import *

data = [{"name": "book1", "author": "author1", "link": "http://www.google.com"},
        {"name": "book2", "author": "author2", "link": "http://www.google.com"},
        {"name": "book2", "author": "author2", "link": "http://www.google.com"}]

class library_Genesis():

    master = None
    data = None

    def __init__(self, data):
        l = extractor()
        self.data = data
        self.master = root
        frame1 = Frame(self.master, cnf={"bg":"#013243"})
        frame1.pack(fill=X)

        self.heading = Label(frame1, cnf={"text":"LIBRARY GENESIS", "bg":"orange", "fg":"White", "justify":"left"})
        self.heading.pack(fill=X)

        self.search_entry = Entry(frame1)
        self.search_entry.pack()

        self.print_button = Button(frame1, text="Search books!", padx="20", bg="#013243")
        self.print_button.bind('<Button-1>', self.create_dataBox)
        self.print_button.pack()

        #self.create_dataBox()

    def Search_books(self, event):
        print(self.search_entry.get())

    def create_dataBox(self, event):
        print("test")
        frame2 = Frame(self.master, cnf={"bg": "#013243", "border":"5"})

        count=0
        for i in data:
            print(i)
            label1 = Label(frame2, text=i['name'], cnf={"bg":"#013243", "fg":"White", "justify":"left"})
            label2 = Label(frame2, text=i['author'], cnf={"bg":"#013243", "fg":"White", "justify":"left"})
            label3 = Label(frame2, text=i['link'], cnf={"bg":"#013243", "fg":"White", "justify":"left"})
            label1.grid(row=0)
            label1.pack(side=LEFT)
            label2.pack(side=LEFT)
            label3.pack(side=LEFT)
            count+=1
        frame2.pack()

root = Tk()
l = library_Genesis(data)
root.config(bg="#013243")
root.minsize(500, 500)
root.title("Hello world!")
root.mainloop()