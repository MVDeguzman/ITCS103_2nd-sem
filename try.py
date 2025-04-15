import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

label= tk.Label(window,text="hello")
label.pack()

entry=tk.Entry()
entry.pack()

button= tk.Button(window, text="click me")
button.pack()

var1=IntVar()
var2=IntVar()

cb1=Checkbutton(window, text="check me", variable=var1)
cb2=Checkbutton(window, text="check me too", variable=var2)

cb1.pack()
cb2.pack()

window.mainloop()

