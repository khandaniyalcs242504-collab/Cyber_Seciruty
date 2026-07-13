import tkinter as tk
from tkinter import messagebox

def encrypt():
    text = entry_text.get()
    key = int(entry_key.get())
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char)-65+key)%26+65)
            else:
                result += chr((ord(char)-97+key)%26+97)
        else:
            result += char

    output.config(text=result)


def decrypt():
    text = entry_text.get()
    key = int(entry_key.get())
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char)-65-key)%26+65)
            else:
                result += chr((ord(char)-97-key)%26+97)
        else:
            result += char

    output.config(text=result)


root = tk.Tk()
root.title("Caesar Cipher")

tk.Label(root, text="Message").pack()

entry_text = tk.Entry(root, width=40)
entry_text.pack()

tk.Label(root, text="Key").pack()

entry_key = tk.Entry(root)
entry_key.pack()

tk.Button(root, text="Encrypt", command=encrypt).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt).pack(pady=5)

output = tk.Label(root, text="", font=("Arial", 12))
output.pack(pady=10)

root.mainloop()
