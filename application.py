# ---------------------------- IMPORTING REQUIRED MODULES ------------------------------- #

import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# A constant for specifying the file to be used for accounts storage
data_file = "data.json"

# Color constants
INPUT = "#27374D"
INPUT_BACKGROUND = "#DDE6ED"
BACKGROUND = "#9DB2BF"
FONT_NAME = "Consolas"
BUTTON = "#526D82"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """
    Takes the specified random numbers, letters, and symbols, and generates a strong password by arranging them randomly.
    """
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

    # Deletes the previous entry of password if user wants to change the password again, and generates new password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    # Copies the entered password to the clipboard.
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    """
    Gets the data of input entry box and checks through that data in json file. Returns the credentials if the website exists in data otherwise displays error.
    """
    website = website_entry.get().title()
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="No data file found!")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(
            title="Oops!", message="No data in the data file yet!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found",
                                message="Desired Data Does not exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save(data_file=data_file):
    """
    Takes the entries data entered in the fields, and save the desired data in a text file. Validates the entries data and warns if any of field remains empty.

    Args:
        data_file (str, optional): A path to a file where you want to save your credentials. Defaults to data_file which will be created in the project directory if it does not exists initially.
    """
    # Takes the data from each entry
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    # If any of field is empty, show warning to the user
    if website == "" or password == "":
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty!")
        return

    # If everything is ok, notify user with the details to be entered before actually entering them in file for better user experience
    is_ok = messagebox.askyesno(
        title=website,
        message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?")

    # If details seem fine to the user
    if is_ok:
        current_data = {
            website: {
                "email": email,
                "password": password
            }
        }

        try:
            with open(data_file, "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            data = current_data
        except json.decoder.JSONDecodeError:
            data = current_data
        else:
            # Updating old data with new data
            data.update(current_data)
        finally:
            # Open the json file for writing purposes and add the details there
            with open(data_file, "w") as file:
                json.dump(data, file, indent=4)

        # Show the message information to user that the record has been entered successfully
        messagebox.showinfo(
            title="Success!", message="Record Entered Successfully!")

        # Deletes the previous records to make entries ready for the new insertion
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
# Create a tkinter window with title and size
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND)

# Use the logo image to be displayed on screen
logo_image = tk.PhotoImage(file="./logo.png")
canvas = tk.Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Create a label for website prompt
website_label = tk.Label(text="Website", font=(
    FONT_NAME, 16), bg=BACKGROUND, fg=INPUT)
website_label.grid(row=1, column=0, sticky="w")

# Create a text box to hold website string
website_entry = tk.Entry(width=25, font=(FONT_NAME, 16), fg=INPUT, bg=INPUT_BACKGROUND)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

search_btn = tk.Button(text="Search", width=18, command=search_password, font=(
    FONT_NAME, 12), bg=BUTTON, fg=INPUT_BACKGROUND)
search_btn.grid(row=1, column=2, sticky="e", pady=5)

# Create a label for email prompt
email_username_label = tk.Label(
    text="Email/Username", font=(FONT_NAME, 16), bg=BACKGROUND, fg=INPUT)
email_username_label.grid(row=2, column=0, sticky="w")

# Create a text box to hold email string
email_username_entry = tk.Entry(
    width=44, font=(FONT_NAME, 16), fg=INPUT, bg=INPUT_BACKGROUND)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_username_entry.insert(
    index=0, string="developer-hassan@yourdeveloper.com")

# Create a label for password prompt
password_label = tk.Label(text="Password", font=(
    FONT_NAME, 16), bg=BACKGROUND, fg=INPUT)
password_label.grid(row=3, column=0, sticky="w")

# Create a text box to hold password string
password_entry = tk.Entry(width=25, font=(FONT_NAME, 16), fg=INPUT, bg=INPUT_BACKGROUND)
password_entry.grid(row=3, column=1, sticky="w")

# Create a button for generating password
generate_password_btn = tk.Button(
    text="Generate Password", width=18, command=generate_password, font=(FONT_NAME, 12), bg=BUTTON, fg=INPUT_BACKGROUND
)
generate_password_btn.grid(row=3, column=2, sticky="e", pady=5)

# Create a button to add details in a text file
add_btn = tk.Button(text="Add", width=52, command=save, font=(
    FONT_NAME, 14), bg=BUTTON, fg=INPUT_BACKGROUND)
add_btn.grid(row=4, column=1, columnspan=3, sticky="w", pady=5)

window.mainloop()
