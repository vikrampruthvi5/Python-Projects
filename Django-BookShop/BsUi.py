"""This is UI for Book shop"""

import tkinter  as tk
from shelf import Shelf

main_cnf = {'bg': '#F2F1EF', 'fg': 'white', 'font': ("Arial-Sans", 20)}
main_bg = {'bg': '#F2F1EF'}
bg_cnf = {'bg': '#95A5A6', 'fg': 'white'}
fg_cnf = {'bg': '#22313F', 'fg': '#ECECEC'}
root = tk.Tk()
var = tk.IntVar()


def build_ui(root):
    frame = tk.Frame(root, cnf={'bg': '#2C3E50'})
    l1 = tk.Label(frame, text="PV Book Shop",
                  cnf={'bg': '#2C3E50', 'fg': '#ECECEC', 'font': ("Arial-Sans", 50)}, ).grid(row=0, column=0)
    frame.configure(cnf={'border': 1})
    frame.pack(fill=tk.X)

    dummy_frame = tk.Frame(root, cnf={'bg': '#F2F1EF'})
    dummy_frame.pack()

    frame1 = tk.Frame(root, cnf={'bg': '#F2F1EF'})
    R1 = tk.Radiobutton(frame1, text="Add book", variable=var, value=1, command=sel, cnf=main_cnf).grid(row=0, column=0,
                                                                                                        sticky=tk.W)
    R1 = tk.Radiobutton(frame1, text="Delete book", variable=var, value=2, command=sel, cnf=main_cnf).grid(row=1,
                                                                                                           column=0,
                                                                                                           sticky=tk.W)
    R1 = tk.Radiobutton(frame1, text="search book", variable=var, value=3, command=sel, cnf=main_cnf).grid(row=2,
                                                                                                           column=0,
                                                                                                           sticky=tk.W)
    frame1.pack(fill=tk.X)

    # Data frame
    dataFrame = tk.Frame(root, cnf={'bg': '#F2F1EF'})
    ret = s.get_books()
    count = 0
    for i in ret:
        l3 = tk.Label(dataFrame, text=str(ret[count][0]), cnf={'bg': '#F2F1EF', 'font': ("Arial-Sans", 18)}).grid(
            row=count, column=0, rowspan=3, sticky=tk.W)
        l4 = tk.Label(dataFrame, text=str(ret[count][1]), cnf={'bg': '#F2F1EF', 'font': ("Arial-Sans", 18)}).grid(
            row=count, column=1, rowspan=3, sticky=tk.W)
        l5 = tk.Label(dataFrame, text=str(ret[count][2]), cnf={'bg': '#F2F1EF', 'font': ("Arial-Sans", 18)}).grid(
            row=count, column=2, rowspan=3, sticky=tk.W)
        print(i)
        count += 1
    dataFrame.pack(fill=tk.X)


def sel():
    sel = var.get()
    if sel is 1:
        add_book = tk.Tk()
    elif sel is 2:
        print(sel)
    elif sel is 3:
        print(sel)


# Building data
s = Shelf()
s.add_book(12093840, "Linux Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
s.add_book(32984579, "Windows Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
s.add_book(10938457, "Python", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
s.add_book(10983530, "Pi Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
s.add_book(32984579, "Windows Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
s.add_book(12093840, "Linux Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
s.add_book(12093840, "Linux Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
s.add_book(12938743, "Linux PRO", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
s.add_book(12093840, "Linux Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
s.add_book(12938743, "Linux PRO", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
s.add_book(86598056, "Linux dig", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
# Shelf().search_isbn(12093840)
# Shelf().get_books()

build_ui(root)
root.title("Book Shop")
root.minsize(1024, 800)
root.configure(cnf=main_bg)
root.mainloop()
