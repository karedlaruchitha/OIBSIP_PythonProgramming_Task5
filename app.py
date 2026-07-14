simport random
import string
import pyperclip
import customtkinter as ctk
from tkinter import messagebox

# ---------------- WINDOW SETUP ---------------- #
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password Generator")
app.geometry("500x500")
app.resizable(False, False)

# ---------------- PASSWORD FUNCTION ---------------- #
def generate_password():
    length = int(length_slider.get())

    characters = ""

    if uppercase_var.get():
        characters += string.ascii_uppercase

    if lowercase_var.get():
        characters += string.ascii_lowercase

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror("Error", "Select at least one character type")
        return

    password = "".join(random.choice(characters) for _ in range(length))

    password_entry.delete(0, "end")
    password_entry.insert(0, password)

    check_strength(password)

# ---------------- PASSWORD STRENGTH ---------------- #
def check_strength(password):
    strength = "Weak"

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        strength = "Weak"

    elif score == 3:
        strength = "Medium"

    else:
        strength = "Strong"

    strength_label.configure(text=f"Strength: {strength}")

# ---------------- COPY FUNCTION ---------------- #
def copy_password():
    password = password_entry.get()

    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard")

# ---------------- UI ---------------- #
title = ctk.CTkLabel(
    app,
    text="Random Password Generator",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

password_entry = ctk.CTkEntry(
    app,
    width=350,
    height=40,
    font=("Arial", 18)
)
password_entry.pack(pady=20)

length_label = ctk.CTkLabel(
    app,
    text="Password Length",
    font=("Arial", 16)
)
length_label.pack()

length_slider = ctk.CTkSlider(
    app,
    from_=4,
    to=32,
    number_of_steps=28
)
length_slider.set(12)
length_slider.pack(pady=10)

uppercase_var = ctk.BooleanVar(value=True)
lowercase_var = ctk.BooleanVar(value=True)
numbers_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=True)

uppercase_check = ctk.CTkCheckBox(
    app,
    text="Uppercase Letters",
    variable=uppercase_var
)
uppercase_check.pack(pady=5)

lowercase_check = ctk.CTkCheckBox(
    app,
    text="Lowercase Letters",
    variable=lowercase_var
)
lowercase_check.pack(pady=5)

numbers_check = ctk.CTkCheckBox(
    app,
    text="Numbers",
    variable=numbers_var
)
numbers_check.pack(pady=5)

symbols_check = ctk.CTkCheckBox(
    app,
    text="Symbols",
    variable=symbols_var
)
symbols_check.pack(pady=5)

generate_button = ctk.CTkButton(
    app,
    text="Generate Password",
    command=generate_password,
    width=200,
    height=40
)
generate_button.pack(pady=20)

copy_button = ctk.CTkButton(
    app,
    text="Copy Password",
    command=copy_password,
    width=200,
    height=40
)
copy_button.pack(pady=10)

strength_label = ctk.CTkLabel(
    app,
    text="Strength: ",
    font=("Arial", 16, "bold")
)
strength_label.pack(pady=10)

# ---------------- RUN APP ---------------- #
app.mainloop()