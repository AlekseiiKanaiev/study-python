#!/usr/bin/python3.5
from tkinter import *
from backend import Database

database = Database('book', 'books.db')

# Alternative of lb.get(ANCHOR)
# bind this function to select event of listbox
# create global variable to call it outside
# plus we fill the entries with the selected row
def get_selected_row(event):
    global selected
    if lb.curselection():
        index = lb.curselection()[0]
        selected = lb.get(index)
        e1.delete(0, END)
        e2.delete(0, END)    
        e3.delete(0, END)
        e4.delete(0, END)
        if isinstance(selected, tuple):
            e1.insert(0, selected[1])
            e2.insert(0, selected[2])
            e3.insert(0, selected[3])
            e4.insert(0, selected[4])

# def window_quit():
#     window.quit()

def delete_all():
    lb.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)    
    e3.delete(0, END)
    e4.delete(0, END)    

def view_all():
    delete_all()
    data = database.view_data()
    if data:
        for line in data:
            lb.insert(END, line)
    else: lb.insert(END, 'No data found')

def search():
    lb.delete(0, END)
    data = []
    if title.get():
        data = database.search_data('title', title.get())
    if author.get():
        data = list(filter(lambda x: author.get().lower() in x[2].lower(), data))\
            if data else database.search_data('author', author.get())
    if year.get().isnumeric():
        data = list(filter(lambda x: year.get() in str(x[3]), data))\
            if data else database.search_data('year', year.get())
    if isbn.get().isnumeric():
        data = list(filter(lambda x: isbn.get() in str(x[4]), data))\
            if data else database.search_data('isbn', isbn.get())
    if data:
        for line in data:
            lb.insert(END, line)
    else:
        lb.insert(0, 'Nothing found or incorect enter parametr')

def add():
    lb.delete(0, END)
    if title.get() and author.get() and year.get() and isbn.get():
        data = {'title': title.get(), 'author': author.get(), 'year': year.get(), 'isbn': isbn.get()}
        view_all() if database.add_data(data) else lb.insert(0, 'Wrong data')
    else:
        lb.insert(END, 'Wrong data')

def update():
    global selected
    # if lb.get(ANCHOR):
    if selected:
        # id = lb.get(ANCHOR)[0]
        id = selected[0]
        if id:
            data = {}
            if title.get(): data['title'] = title.get()
            if author.get(): data['author'] = author.get()
            if year.get().isdigit(): data['year'] = year.get()
            if isbn.get().isdigit(): data['isbn'] = isbn.get()
            if data:
                database.update_data(id, data)
                view_all()
                selected = ''
            else:
                lb.delete(0, END)
                lb.insert(END, 'No new data enter or incorrect data')
    else:
        lb.delete(0, END)
        lb.insert(END, 'No string selected')


def delete():
    global selected
    # if lb.get(ANCHOR):
    if selected:
        if chvar.get():
            # id = lb.get(ANCHOR)[0]
            id = selected[0]
            if id:
                database.delete_data(id)
                view_all()
                chvar.set(False)
                selected = ''
        else:
            lb.delete(ANCHOR)
            selected = ''
    else:
        lb.delete(0, END)
        lb.insert(END, 'No string selected')    

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

lb = Listbox(window, height = 12, width = 40)
lb.grid(rowspan = 7, columnspan = 2, row = 2, column = 0)

sb = Scrollbar(window)
sb.grid(column = 2, row = 2, rowspan = 7)
# binding scrollbar to textfiel
sb['command'] = lb.yview
lb['yscrollcommand'] = sb.set

# binding new function to listbox (create new method)
lb.bind('<<ListboxSelect>>', get_selected_row)

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

chvar = BooleanVar()
chvar.set(0)
ch = Checkbutton(window, text = 'Delete from DB', variable = chvar, onvalue = True, offvalue = False)
ch.grid(row = 7, column = 3)

b1 = Button(window, text = 'Close', width = 12, command = window.destroy)
b1.grid(row = 8, column = 3)



window.mainloop()