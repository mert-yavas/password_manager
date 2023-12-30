from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def new_password():
    """
    Generate a new password and copy it to the clipboard.
    """
    password_entry.delete(0, END)
    get_password = password_generator()
    pyperclip.copy(get_password)
    password_entry.insert(0, f"{get_password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_passwords():
    """
    Save the entered website, email, and password to a file.
    """
    website = website_entry.get()
    email = mail_entry.get()
    password = password_entry.get()
    if website == "" or password == "":
        messagebox.showwarning("Opps", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel("website", message=f"These are the details entered: \nEmail: {email}"
                                                  f"\nPassword:{password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as ids_and_passwords:
                ids_and_passwords.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# website_label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# website entry
website_entry = Entry(width=53)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()

# mail_label
mail_label = Label(text="Email/Username:")
mail_label.grid(row=2, column=0)

# mail entry
mail_entry = Entry(width=53)
mail_entry.grid(row=2, column=1, columnspan=2, sticky="W")
mail_entry.insert(0, "example@example.com")

# password_label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# password entry
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="W")

# password button
password_button = Button(text="Generate Password", command=new_password)
password_button.grid(row=3, column=2, sticky="W")

# add button
add_button = Button(text="Add", width=45, command=save_passwords)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()
