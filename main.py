from tkinter import *
from tkinter import messagebox
import bz2
import binascii
import os
import copy

master = Tk()

v = IntVar()
a =[]
def func3():
    
    print("compression and deccompression using bzip2")
    x=input("Enter file name : ")
    z=str(x).split('.')
    a=copy.copy(z)
    inF = open(x, 'rb')
    s = inF.read()
    inF.close()

    outF=bz2.BZ2File("compressedByBZ2.bz",'wb')
    outF.write(s)
    outF.close()

def func4():
    inF = bz2.BZ2File("compressedByBZ2.bz", 'rb')
    s = inF.read()
    inF.close()

    outF = open("x1."+str(a[1]), 'wb')
    outF.write(s)
    outF.close()

    

def func2():
    Label(
      text="""compression and deccompression using bzip2""",
      justify = LEFT,
      padx = 20).pack()

    Radiobutton(
            text="compress a file",
            padx = 20, 
            variable=v, 
            value=6,command=func3).pack(anchor=W)
    Radiobutton(
            text="(de)compress a file ",
            padx = 20, 
            variable=v, 
            value=7,command=func4).pack(anchor=W)
    Radiobutton( 
            text="Upload file to drive",
            padx = 20, 
            variable=v, 
            value=8).pack(anchor=W)
    Radiobutton(
            text="exit",
            padx = 20, 
            variable=v, 
            value=9).pack(anchor=W)
            

def func1():
    messagebox.showinfo("one","compression and deccompression using bzip2")


Label(master, 
      text="""Enter the type of compression you want do:""",
      justify = LEFT,
      padx = 20).pack()
Radiobutton(master, 
            text="Enter the filename as 'fortar.py' for archieving:",
            padx = 20, 
            variable=v, 
            value=1,
            command=func1).pack(anchor=W)
Radiobutton(master, 
            text="Enter the filename as 'forbz2.py' for bz2 compression: ",
            padx = 20, 
            variable=v, 
            value=2,
            command=func2).pack(anchor=W)
Radiobutton(master, 
            text="Enter the filename as 'forgzip.py' for gzip compression: ",
            padx = 20, 
            variable=v, 
            value=3,
            command=func1).pack(anchor=W)
Radiobutton(master, 
            text="Enter the filename as 'forlzma.py' for lzma compression:",
            padx = 20, 
            variable=v, 
            value=4,
            command=func1).pack(anchor=W)
Radiobutton(master, 
            text="Want to see user selection stats (y/n)?",
            padx = 20, 
            variable=v, 
            value=5,
            command=func1).pack(anchor=W)


mainloop()
  
