import tkinter as tk
from tkinter import ttk

import isbn_validator as isbn_validator


def fun():
    print(isbn_validator.validate_isbn(search_entry.get()))

root=tk.Tk()
root.title("ISBN-legitimations Prüfer")
root.geometry("800x600")
root.configure(background="grey")


style = ttk.Style()
style.configure(".", foreground="Black", background="grey",font=("Arial", 12)) 

first_frame=ttk.Frame(root)
first_frame.pack(pady=20)


search_entry= ttk.Entry(first_frame,width=70,)
start_lable=ttk.Label(first_frame,text="Gib die zu prüfende ISBN-Nummer ein:")
strat_button=ttk.Button(first_frame,)

start_lable.pack(side="left")
search_entry.pack(side="left")
strat_button.pack(side="right")

root.bind('<Return>',lambda event: fun())
