from tkinter import *
import tkinter.messagebox as box

def dialog1():
    username=entry1.get()
    password = entry2.get()
    if (username == 'admin' and  password == 'secret'):
        box.showinfo('info','Correct Login')
    else:
        box.showinfo('info','Invalid Login')


window = Tk()
window.title('Admin paneli')

frame = Frame(window)

Label1 = Label(window,text = 'Username:')
Label1.pack(padx=15,pady= 5)

entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)



Label2 = Label(window,text = 'Password: ' )
Label2.pack(padx = 15,pady=6)

entry2 = Entry(window, bd=5)
entry2.pack(padx = 15,pady=7)

btn = Button(frame, text = 'Check Login',command = dialog1)


btn.pack(side = RIGHT , padx =5)
frame.pack(padx=100,pady = 19)
window.mainloop()
