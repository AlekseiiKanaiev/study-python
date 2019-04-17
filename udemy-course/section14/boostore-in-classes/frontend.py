#!/usr/bin/python3.5
from tkinter import *
from backend import Database

database = Database('book', 'books.db')

class Bookstore():
    
    def __init__(self, window):
        self.window = window
        self.window.title('Booksore')
        self.window.resizable(False, False)

        self.selected = ''

        l1 = Label(window, text = 'Title')
        l1.grid(row = 0, column = 0)

        self.title = StringVar()
        self.e1 = Entry(window, textvariable = self.title)
        self.e1.grid(row = 0, column = 1)

        l2 = Label(window, text = 'Author')
        l2.grid(row = 0, column = 2)

        self.author = StringVar()
        self.e2 = Entry(window, textvariable = self.author)
        self.e2.grid(row = 0, column = 3)

        l3 = Label(window, text = 'Year')
        l3.grid(row = 1, column = 0)

        self.year = StringVar()
        self.e3 = Entry(window, textvariable = self.year)
        self.e3.grid(row = 1, column = 1)

        l4 = Label(window, text = 'ISBN')
        l4.grid(row = 1, column = 2)

        self.isbn = StringVar()
        self.e4 = Entry(window, textvariable = self.isbn)
        self.e4.grid(row = 1, column = 3)

        self.lb = Listbox(window, height = 12, width = 40)
        self.lb.grid(rowspan = 7, columnspan = 2, row = 2, column = 0)

        sb = Scrollbar(window)
        sb.grid(column = 2, row = 2, rowspan = 7)
        # binding scrollbar to textfiel
        sb['command'] = self.lb.yview
        self.lb['yscrollcommand'] = sb.set

        # binding new function to listbox (create new method)
        self.lb.bind('<<ListboxSelect>>', self.get_selected_row)

        b1 = Button(window, text = 'View All', width = 12, command = self.view_all)
        b1.grid(row = 2, column = 3)

        b2 = Button(window, text = 'Search Entry', width = 12, command = self.search)
        b2.grid(row = 3, column = 3)

        b3 = Button(window, text = 'Add Entry', width = 12, command = self.add)
        b3.grid(row = 4, column = 3)

        b1 = Button(window, text = 'Update Selected', width = 12, command = self.update)
        b1.grid(row = 5, column = 3)

        b1 = Button(window, text = 'Delete Selected', width = 12, command = self.delete)
        b1.grid(row = 6, column = 3)

        self.chvar = BooleanVar()
        self.chvar.set(False)
        ch = Checkbutton(window, text = 'Delete from DB', variable = self.chvar, onvalue = True, offvalue = False)
        ch.grid(row = 7, column = 3)

        self.b1 = Button(window, text = 'Close', width = 12, command = window.destroy)
        self.b1.grid(row = 8, column = 3)

    def delete_all_entry(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)    
        self.e3.delete(0, END)
        self.e4.delete(0, END)    

    # Alternative of lb.get(ANCHOR)
    # bind this function to select event of listbox
    # create global variable to call it outside
    # plus we fill the entries with the selected row
    def get_selected_row(self, event):
        if self.lb.curselection():
            index = self.lb.curselection()[0]
            self.selected = self.lb.get(index)
            self.delete_all_entry()
            if isinstance(self.selected, tuple):
                self.e1.insert(0, self.selected[1])
                self.e2.insert(0, self.selected[2])
                self.e3.insert(0, self.selected[3])
                self.e4.insert(0, self.selected[4])

    def view_all(self):
        self.lb.delete(0, END)
        self.delete_all_entry()
        data = database.view_data()
        if data:
            for line in data:
                self.lb.insert(END, line)
        else: self.lb.insert(END, 'No data found')

    def search(self):
        self.lb.delete(0, END)
        data = []
        if self.title.get():
            data = database.search_data('title', self.title.get())
        if self.author.get():
            data = list(filter(lambda x: self.author.get().lower() in x[2].lower(), data))\
                if data else database.search_data('author', self.author.get())
        if self.year.get().isnumeric():
            data = list(filter(lambda x: self.year.get() in str(x[3]), data))\
                if data else database.search_data('year', self.year.get())
        if self.isbn.get().isnumeric():
            data = list(filter(lambda x: self.isbn.get() in str(x[4]), data))\
                if data else database.search_data('isbn', self.isbn.get())
        if data:
            for line in data:
                self.lb.insert(END, line)
        else:
            self.lb.insert(0, 'Nothing found or incorect enter parametr')

    def add(self):
        self.lb.delete(0, END)
        if self.title.get() and self.author.get() and self.year.get() and self.isbn.get():
            data = {'title': self.title.get(), 'author': self.author.get(), 'year': self.year.get(), 'isbn': self.isbn.get()}
            self.view_all() if database.add_data(data) else self.lb.insert(0, 'Wrong data')
        else:
            self.lb.insert(END, 'Wrong data')

    def update(self):
        if self.selected:
            id = self.selected[0]
            if id:
                data = {}
                if self.title.get(): data['title'] = self.title.get()
                if self.author.get(): data['author'] = self.author.get()
                if self.year.get().isdigit(): data['year'] = self.year.get()
                if self.isbn.get().isdigit(): data['isbn'] = self.isbn.get()
                if data:
                    database.update_data(id, data)
                    self.view_all()
                    self.selected = ''
                else:
                    self.lb.delete(0, END)
                    self.lb.insert(END, 'No new data enter or incorrect data')
        else:
            self.lb.delete(0, END)
            self.lb.insert(END, 'No string selected')


    def delete(self):
        if self.selected:
            if self.chvar.get():
                id = self.selected[0]
                if id:
                    database.delete_data(id)
                    self.view_all()
                    self.chvar.set(False)
                    self.selected = ''
            else:
                self.lb.delete(ANCHOR)
                self.selected = ''
        else:
            self.lb.delete(0, END)
            self.lb.insert(END, 'No string selected')    

window = Tk()
bookstore = Bookstore(window)
window.mainloop()