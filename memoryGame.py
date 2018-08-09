from tkinter import *
from random import random
import time
from tkinter import messagebox

pencere = Tk()
pencere.title("myGame")
pencere.geometry('180x180')

icerikler = ['ebru','arslan','KTU','game',4,'computer','engineer','linux']
print(icerikler)
icerikler = icerikler*2
print(icerikler)

satirNo=0
for satir in range (0,4):
    sutunNo = 0
    for sutun in range (0,4):
        butonBas = Button(pencere, text="match")
        butonBas.grid(row = satirNo , column = sutunNo)
        sutunNo += 1
    satirNo += 1

pencere.mainloop()
