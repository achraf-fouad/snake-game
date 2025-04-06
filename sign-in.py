import tkinter as tk

def login():
    user = username.get()
    pwd = password.get()
    if user == "admin" and pwd == "1234":
        result.config(text="Login successful")
    else:
        result.config(text="Invalid credentials")

root = tk.Tk()
root.title("Sign In")

tk.Label(root, text="Username").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack()
password = tk.Entry(root, show="*")
password.pack()

tk.Button(root, text="Login", command=login).pack()
result = tk.Label(root, text="")
result.pack()

root.mainloop()
