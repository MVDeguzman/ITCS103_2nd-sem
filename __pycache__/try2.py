
import tkinter as tk

window = tk.Tk()
window.title("Log in")

# Create a frame to hold the username label and entry
username_frame = tk.Frame(window)
username_frame.pack(pady=5)

# Username Label
username_label = tk.Label(username_frame, text="Username", width=10, anchor="w")
username_label.pack(side="left", padx=(0, 5))  # Add some padding to the right of the label

# Username Entry
username_entry = tk.Entry(username_frame)
username_entry.pack(side="left", fill="x", expand=True)

# Create a frame to hold the password label and entry
password_frame = tk.Frame(window)
password_frame.pack(pady=5)

# Password Label
password_label = tk.Label(password_frame, text="Password", width=10, anchor="w")
password_label.pack(side="left", padx=(0, 5))  # Add some padding to the right of the label

# Password Entry
password_entry = tk.Entry(password_frame, show="*")
password_entry.pack(side="left", fill="x", expand=True)

window.mainloop()