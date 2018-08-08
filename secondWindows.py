from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("FirstWindows")
lbl = Label(window , text="kullanıcı arayüzü",font=("Arial-bold", 30))
window.geometry('500x500')
combo = Combobox( window )
combo['values'] = (1,2,3,4,'ebru')
combo.grid(column=5,row=4)
txt= Entry(window, width=10)
txt.grid(column=5 , row=5)
def cliked():
    res = "it was here" + txt.get()
    lbl.configure(text= res)
lbl.grid(column=5,row=2)
"""btn = Button(window, text="click", bg="green", fg="white" ,command= cliked)
btn.grid(column=5,row=6)"""
window.mainloop()
