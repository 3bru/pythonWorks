"""Ebru ARSLAN
    13/08/2018
"""
from tkinter import *
from random import random
import time
from tkinter import messagebox

pencere = Tk()
pencere.title("myGame")
pencere.geometry('280x180')

atama=[]
memory = []
bilinen = 0

def cevir(a):
    if len(memory)==0:
        for i in atama:
            if a==i[0]:
                ilkButon = i[2]
                ilkButon.config(text=i[1], state="disable")
                memory.append(i)
                print(memory)
    else:
        for i in atama:
            if a ==i[0]:
                ikinciButon=i[2]
                ikinciButon.config(text=i[1], state="disable")
                if i[1]==memory[0][1]:
                    memory.clear()
                else:
                    ikinciButon.after(100, lambda x=i[2]:cevirici(x))

def cevirici(ikinciButon):
    ilkButon = memory[0][2]
    ilkButon.config(text="find match", state="active")
    ikinciButon.config(text="find match", state="active")
    time.sleep(0.5)
    memory.clear()

icerikler = ['ebru','arslan','ktü','computer','engineer',4,'python','c++']
#print(icerikler)
icerikler = icerikler*2
#print(icerikler)
satirNo=0
for satir in range (0,4):
    sutunNo = 0
    for sutun in range (0,4):
        deger = len(icerikler)
        first = str(satirNo) + str(sutunNo)
        second = int(random()*deger)
#        print(icerikler[second])
        butonBas = Button(pencere, text="match", command = lambda a = first : cevir(a))
        atanacak = (first,icerikler[second],butonBas)
        atama.append(atanacak)
        icerikler.pop(second)
        butonBas.grid(row = satirNo , column = sutunNo)
        sutunNo += 1
    satirNo += 1
pencere.mainloop()
