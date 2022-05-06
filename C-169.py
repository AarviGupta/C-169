# -*- coding: utf-8 -*-
"""
Created on Fri May  6 12:18:16 2022

@author: HP
"""

from tkinter import *
root=Tk()
root.title("Classes")
root.geometry("900x600")

class createelements:
    def __init__(self):
        print("This is create elements class")
    def createnewelement(self):
        label=Label(root,text="A new label is created using class",fg="red")
        label.pack()
        button=Button(root,text="Show message",command=self.message)
        button.pack(padx=20,pady=20)
    def message(self):
        messagebox.showinfo("Show info","You clicked the button created using class.")
        
object1=createelements()
btn=Button(root,text="Click me to create label and button element",command=object1.createnewelement)  
btn.pack(padx=20,pady=20)      

root.mainloop()