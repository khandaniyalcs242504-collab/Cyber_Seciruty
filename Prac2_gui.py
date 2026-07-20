import tkinter as tk
from tkinter import messagebox

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def rsa_process():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        e = int(entry_e.get())
        message = entry_message.get()

        n = p * q
        phi = (p - 1) * (q - 1)

        if gcd(e, phi) != 1:
            messagebox.showerror("Error", "e must be coprime with φ(n)")
            return

        d = mod_inverse(e, phi)

        encrypted = []

        for ch in message:
            encrypted.append(pow(ord(ch), e, n))

        decrypted = ""

        for num in encrypted:
            decrypted += chr(pow(num, d, n))

        output.config(
            text=f"Public Key : ({e}, {n})\n\n"
                 f"Private Key : ({d}, {n})\n\n"
                 f"Encrypted : {encrypted}\n\n"
                 f"Decrypted : {decrypted}"
        )

    except Exception:
        messagebox.showerror("Error", "Enter valid values.")

root = tk.Tk()
root.title("RSA Encryption & Decryption")
root.geometry("500x500")

tk.Label(root, text="Prime Number (p)").pack()
entry_p = tk.Entry(root)
entry_p.pack()

tk.Label(root, text="Prime Number (q)").pack()
entry_q = tk.Entry(root)
entry_q.pack()

tk.Label(root, text="Public Exponent (e)").pack()
entry_e = tk.Entry(root)
entry_e.pack()

tk.Label(root, text="Message").pack()
entry_message = tk.Entry(root, width=40)
entry_message.pack()

tk.Button(root, text="Encrypt & Decrypt", command=rsa_process).pack(pady=10)

output = tk.Label(root, justify="left", font=("Arial", 10))
output.pack()

root.mainloop()
