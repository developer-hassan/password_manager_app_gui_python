# ---------------------------- IMPORTING REQUIRED MODULES ------------------------------- #

import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

data_file = "data.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # List to hold alphabets in both cases
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    # List to hold numbers
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # List to hold the symbols
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    # User inputs
    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)

    # Declaring the password string
    password = ""

    # Appending letters in password list
    password_letters = [random.choice(letters) for _ in range(num_letters)]
    password += "".join(password_letters)

    #   Appending symbols in password list
    password_symbols = [random.choice(symbols) for _ in range(num_symbols)]
    password += "".join(password_symbols)

    # Appending numbers in password list
    password_numbers = [random.choice(numbers) for _ in range(num_numbers)]
    password += "".join(password_numbers)

    # Using random.sample() to choose the random sample of password length
    password = "".join(random.sample(password, len(password)))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save(data_file=data_file):
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showwarning(
            title="Oops!", message="Please don't leave any fields empty!"
        )
        return

    is_ok = messagebox.askyesno(
        title=website,
        message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?",
    )

    if is_ok:
        with open(data_file, "a") as file:
            file.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_image = tk.PhotoImage(file="./logo.png")
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website: ")
website_label.grid(row=1, column=0)

website_entry = tk.Entry(width=43)
website_entry.grid(row=1, column=1, columnspan=3, sticky="w")
website_entry.focus()

email_username_label = tk.Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

email_username_entry = tk.Entry(width=43)
email_username_entry.grid(row=2, column=1, columnspan=3, sticky="w")
email_username_entry.insert(index=0, string="youremail@example.com")

password_label = tk.Label(text="Password: ")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(width=22)
password_entry.grid(row=3, column=1, sticky="w")

generate_password_btn = tk.Button(
    text="Generate Password", width=16, command=generate_password
)
generate_password_btn.grid(row=3, column=1, columnspan=2, sticky="e")

add_btn = tk.Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="w")


window.mainloop()
