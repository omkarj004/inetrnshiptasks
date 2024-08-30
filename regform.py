import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    # You can save this information or perform any other action here
    # For now, let's just display a message box with the entered details
    messagebox.showinfo("Registration Successful", f"Name: {name}\nEmail: {email}\nAge: {age}")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create form fields
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root)

age_label = tk.Label(root, text="Age:")
age_entry = tk.Entry(root)

submit_button = tk.Button(root, text="Submit", command=submit_form)

# Arrange widgets using grid layout
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry.grid(row=0, column=1, padx=10, pady=5)

email_label.grid(row=1, column=0, padx=10, pady=5)
email_entry.grid(row=1, column=1, padx=10, pady=5)

age_label.grid(row=2, column=0, padx=10, pady=5)
age_entry.grid(row=2, column=1, padx=10, pady=5)

submit_button.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
