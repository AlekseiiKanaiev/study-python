#!/usr/bin/python3.5

from tkinter import *

def km_to_miles():
    t1.delete(1.0, END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)
    try:
        r = float(e1_val.get())
    except:
        r = 'NaN'
    t1.insert(INSERT, r if r == 'NaN' else round(r*1000, 2))
    t2.insert(INSERT, r if r == 'NaN' else round(r*2.20462 , 2))
    t3.insert(INSERT, r if r == 'NaN' else round(r*35.274, 2))
    

window = Tk()
m = Label(window, text = 'kg', justify = LEFT)
m.grid(row =0, column = 0)

m1 = Label(window, text = 'grams')
m1.grid(row =1, column = 0)

m2 = Label(window, text = 'pounds')
m2.grid(row =1, column = 1)

m3 = Label(window, text = 'ounces')
m3.grid(row =1, column = 2)

b1 = Button(window, text = 'Execute', command = km_to_miles)
b1.grid(row = 0, column = 2)

e1_val = StringVar()
e1 = Entry(window, textvariable = e1_val)
e1.grid(row = 0, column = 1)

t1 = Text(window, height = 1, width = 25)
t1.grid(row = 2, column = 0)

t2 = Text(window, height = 1, width = 25)
t2.grid(row = 2, column = 1)

t3 = Text(window, height = 1, width = 25)
t3.grid(row = 2, column = 2)

# without it the window will open and close in 1s
window.mainloop()

