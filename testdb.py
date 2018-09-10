from tkinter import *
from tkinter import ttk
import sqlite3

class Product:
    db_name = "database.db"
    def __init__(self,wind):
        self.wind = wind
        self.wind.title('IT products')

        frame = LabelFrame(self.wind, text="add new record")
        frame.grid(row=0, column=1)

        Label(frame, text='Name:').grid(row=1, column=1)
        self.name = Entry(frame)
        self.name.grid(row=1, column=2)

        ttk.Button(frame, text='price').grid(row=2, column=1)
        self.price = Entry(frame)
        self.price.grid(row=2, column=2)

        ttk.Button(frame, text='Add record').grid(row=2, column=2)
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0)

        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0',text='Name', anchor=W)
        self.tree.heading(2, text='Price', anchor=W)

        ttk.Button(text='Delete record').grid(row=5, column=0)
        ttk.Button(text='Edir record').grid(row=5,column=1)




if __name__ == '__main__':
    wind = Tk()
    application = Product(wind)
    wind.mainloop()
