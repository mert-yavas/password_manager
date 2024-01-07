from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import json
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
    website = website_entry.get().lower()
    email = mail_entry.get()
    password = password_entry.get()
    new_data = {website: {
                    "email": email,
                    "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showwarning("Opps", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving updated
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORDS ------------------------------- #


def search_passwords():
    website = website_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            # reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            show_password = data[website]["password"]
            show_email = data[website]["email"]
            messagebox.showinfo(title=website, message=f"Email: {show_email}\nPassword: {show_password} ")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


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
website_entry = Entry(width=35)
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

# search button
search_button = Button(text="Search", width=14, command=search_passwords)
search_button.grid(row=1, column=2, sticky="W")

# add button
add_button = Button(text="Add", width=45, command=save_passwords)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()
