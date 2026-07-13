import tkinter as tk

# ---------- Encrypt Function ----------
def encrypt(text, key):
    rail = ['' for _ in range(key)]
    direction = 1
    row = 0

    for ch in text:
        rail[row] += ch

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return ''.join(rail)

# ---------- Decrypt Function ----------
def decrypt(cipher, key):
    pattern = [['' for _ in cipher] for _ in range(key)]

    row = 0
    direction = 1

    for col in range(len(cipher)):
        pattern[row][col] = '*'

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    index = 0

    for i in range(key):
        for j in range(len(cipher)):
            if pattern[i][j] == '*':
                pattern[i][j] = cipher[index]
                index += 1

    result = ""

    row = 0
    direction = 1

    for col in range(len(cipher)):
        result += pattern[row][col]

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return result


# ---------- GUI ----------
def gui_encrypt():
    result.config(text=encrypt(text_entry.get(), int(key_entry.get())))

def gui_decrypt():
    result.config(text=decrypt(text_entry.get(), int(key_entry.get())))

root = tk.Tk()
root.title("Rail Fence Cipher")

tk.Label(root, text="Message").pack()

text_entry = tk.Entry(root, width=40)
text_entry.pack()

tk.Label(root, text="Number of Rails").pack()

key_entry = tk.Entry(root)
key_entry.pack()

tk.Button(root, text="Encrypt", command=gui_encrypt).pack(pady=5)

tk.Button(root, text="Decrypt", command=gui_decrypt).pack(pady=5)

result = tk.Label(root, text="", font=("Arial",12))
result.pack(pady=10)

root.mainloop()
