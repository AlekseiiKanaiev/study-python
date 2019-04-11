#!/usr/bin/python3.5
from tkinter import *
from backend import *

def window_quit():
    window.quit()

def delete_all():
    t.delete(1.0, END)
    e1.delete(0, END)
    e2.delete(0, END)    
    e3.delete(0, END)
    e4.delete(0, END)    

def view_all():
    delete_all()
    data = view_data()
    if data:
        for line in data:
            # line.append('\n')
            s = '--'.join(list(map(lambda x: str(x), line)))+'\n'
            t.insert(END, s)

def search():
        t.delete(1.0, END)
        if title.get():
            data = search_data('title', title.get())
        elif author.get():
            data = search_data('author', author.get())
        elif year.get().isnumeric():
            data = search_data('year', year.get())
        elif isbn.get().isnumeric():
            data = search_data('isbn', isbn.get())
        else:
            t.insert(1.0, 'No search parametr enter or incorect parametr enter')
            return
        if data:
            if title.get():
                # data = list(map(lambda el: filter(lambda x: title.get() in x, el), data))
                data = list(filter(lambda x: title.get() in x[1], data))
            if author.get():
                data = list(filter(lambda x: author.get() in x[2], data))
            if year.get():
                data = list(filter(lambda x: year.get() in str(x[3]), data))
            if isbn.get():
                data = list(filter(lambda x: isbn.get() in str(x[4]), data))
            for line in data:
                s = '--'.join(list(map(lambda x: str(x), line)))+'\n'
                t.insert(END, s)
        else:
            t.insert(1.0, 'Nothing found')

def add():
        t.delete(1.0, END)
        if title.get() and author.get() and year.get() and isbn.get():
            data = {'id': max(view_data())[0]+1, 'title': title.get(), 'author': author.get(), 'year': year.get(), 'isbn': isbn.get()}
        #     print(add_data(data))
            view_all() if add_data(data) else t.insert(1.0, 'Wrong data')
        else:
            t.insert(1.0, 'Wrong data')

def update():
        delete_all()
        print(t.selection_get())

def delete():
        delete_all()
        pass

window = Tk()
window.title('Booksore')
window.resizable(False, False)

l1 = Label(window, text = 'Title')
l1.grid(row = 0, column = 0)

title = StringVar()
e1 = Entry(window, textvariable = title)
e1.grid(row = 0, column = 1)

l2 = Label(window, text = 'Author')
l2.grid(row = 0, column = 2)

author = StringVar()
e2 = Entry(window, textvariable = author)
e2.grid(row = 0, column = 3)

l3 = Label(window, text = 'Year')
l3.grid(row = 1, column = 0)

year = StringVar()
e3 = Entry(window, textvariable = year)
e3.grid(row = 1, column = 1)

l4 = Label(window, text = 'ISBN')
l4.grid(row = 1, column = 2)

isbn = StringVar()
e4 = Entry(window, textvariable = isbn)
e4.grid(row = 1, column = 3)

t = Text(window, height = 12, width = 40, wrap = WORD)
t.grid(rowspan = 6, columnspan = 2)

b1 = Button(window, text = 'View All', width = 12, command = view_all)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = 'Search Entry', width = 12, command = search)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = 'Add Entry', width = 12, command = add)
b3.grid(row = 4, column = 3)

b1 = Button(window, text = 'Update Selected', width = 12, command = update)
b1.grid(row = 5, column = 3)

b1 = Button(window, text = 'Delete Selected', width = 12, command = delete)
b1.grid(row = 6, column = 3)

b1 = Button(window, text = 'Close', width = 12, command = window_quit)
b1.grid(row = 7, column = 3)

window.mainloop()