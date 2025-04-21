import  tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x400")
window.title("ITCS103 TKINTER!")

frame1= tk.Frame()
frame2= tk.Frame()

frame1.pack()
frame2.pack()
 
label = Label(frame1,text = "CATEGORY", font=("Arial", 20, "bold"), fg="black") 
label.pack()  

text= tk.Text(frame1,width=30, height=5, font=("Arial", 12), bg="lightblue")
text.insert(1.0, "What is the common programming language in BSIT first year?")
text.pack(pady=30)
   
listbox = tk.Listbox(frame1, width=30, height=5,font=("Arial", 12),bg="lightblue")
   
listbox.insert(1,"C++")  
listbox.insert(2, "Python")  
listbox.insert(3, "Java")  
listbox.insert(4, "HTML")
listbox.insert(5, "CSS")  
   
listbox.pack(pady=30)  
window.mainloop()



