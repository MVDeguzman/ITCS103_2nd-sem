import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Calc")
window.geometry('450x425')

# Frames
frame = tk.Frame()
sep_frame = tk.Frame()

# Widgets
# Login Label
login_label = tk.Label(frame, text="Log in", font=("Arial", 30))

# Entries
user_entry = tk.Entry(frame, font=("Arial", 19))
pass_entry = tk.Entry(frame, font=("Arial", 19))

# User and Pass Label
user_label = tk.Label(user_entry, text="Username", font=("Arial", 15), width= 33, bg= "white", fg= "gray58")
pass_label = tk.Label(pass_entry, text="Password", font=("Arial", 15), width= 33, bg= "white", fg= "gray58")

# Login Button
log_button = tk.Button(frame, text="Log in", font=("Arial", 15), bg= "dodgerblue2", fg= "white", width= 33)

# Remember Me Checkbutton
var1 = IntVar()
rem_cb = tk.Checkbutton(frame, text="Remember Me", variable=var1, font=("Arial", 12))

# Forget and Create Label
forgpass_label = tk.Label(frame, text="Forgot Password?", fg= "dodgerblue2", font=("Arial", 12))
create_label = tk.Label(sep_frame, text="Create an Account", fg= "dodgerblue2", font=("Arial", 12))


# Packing
login_label.pack(pady=20)

user_entry.pack(pady=8)
pass_entry.pack(pady=8)
user_label.pack(pady=3)
pass_label.pack(pady=3)

log_button.pack(pady=8)

rem_cb.pack(side="left")
forgpass_label.pack(side="right")
create_label.pack(pady=45)

frame.pack()
sep_frame.pack()


window.mainloop()