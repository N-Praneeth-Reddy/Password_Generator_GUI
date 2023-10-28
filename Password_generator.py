import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    password_length = int(length_var.get())
    if password_length <= 0:
        result_label.config(text="Invalid length")
        return

    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    if not (use_lowercase or use_uppercase or use_digits or use_special):
        result_label.config(text="Select at least one character type")
        return

    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if len(characters) == 0:
        result_label.config(text="No characters selected")
        return

    password = ''.join(random.choice(characters) for _ in range(password_length))
    result_label.config(text=password)
    update_password_strength(password)

def update_password_strength(password):
    strength = 0
    if any(c in string.ascii_lowercase for c in password):
        strength += 1
    if any(c in string.ascii_uppercase for c in password):
        strength += 1
    if any(c in string.digits for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if len(password) >= 12 and strength >= 3:
        strength_label.config(text="Strong", foreground="green")
    elif len(password) >= 8 and strength >= 2:
        strength_label.config(text="Moderate", foreground="orange")
    else:
        strength_label.config(text="Weak", foreground="red")

def save_password():
    password = result_label.cget("text")
    if not password:
        return

    file_path = file_path_var.get()
    if file_path:
        with open(file_path, "a") as file:
            file.write(password + "\n")
        save_result_label.config(text="Password saved to file", foreground="green")
    else:
        save_result_label.config(text="Enter a valid file path", foreground="red")

root = tk.Tk()
root.title("Password Generator")

options_frame = ttk.LabelFrame(root, text="Password Options")
options_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

ttk.Label(options_frame, text="Password Length:").grid(row=0, column=0, sticky="w")
length_var = tk.StringVar()
length_entry = ttk.Entry(options_frame, textvariable=length_var)
length_entry.grid(row=0, column=1, padx=10)
length_var.set(12)

ttk.Label(options_frame, text="Include:").grid(row=1, column=0, sticky="w")
lowercase_var = tk.IntVar()
ttk.Checkbutton(options_frame, text="Lowercase", variable=lowercase_var).grid(row=1, column=1, sticky="w")
uppercase_var = tk.IntVar()
ttk.Checkbutton(options_frame, text="Uppercase", variable=uppercase_var).grid(row=1, column=2, sticky="w")
digits_var = tk.IntVar()
ttk.Checkbutton(options_frame, text="Digits", variable=digits_var).grid(row=1, column=3, sticky="w")
special_var = tk.IntVar()
ttk.Checkbutton(options_frame, text="Special Characters", variable=special_var).grid(row=1, column=4, sticky="w")

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, padx=10, pady=10)

strength_label = ttk.Label(root, text="", font=("Arial", 12))
strength_label.grid(row=2, column=0, padx=10, pady=5)

save_result_label = ttk.Label(root, text="", font=("Arial", 12))
save_result_label.grid(row=3, column=0, padx=10, pady=5)

ttk.Label(options_frame, text="File Path:").grid(row=4, column=0, sticky="w")
file_path_var = tk.StringVar()
file_path_entry = ttk.Entry(options_frame, textvariable=file_path_var)
file_path_entry.grid(row=4, column=1, padx=10)

save_button = ttk.Button(root, text="Save Password to File", command=save_password)
save_button.grid(row=5, column=0, padx=10, pady=5)

result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=6, column=0, padx=10, pady=10)

root.mainloop()