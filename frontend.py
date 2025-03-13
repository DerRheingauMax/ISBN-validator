import tkinter as tk
from tkinter import ttk

import isbn_validator as isbn_validator

block = False

def fun():
    global block
    if block: 
        block = False
        return 
    result_label.config(text="", foreground="green", background="grey") 
    root.configure(background="grey")
    fehler_label.config(text="", foreground="red")

def run():
    global block
    block = True
    result, error =isbn_validator.validate_isbn(search_entry.get())

    if result:
        root.configure(background="grey")
        result_label.config(text=" Gültige ISBN", foreground="green", background="grey") 
    else:
        root.configure(background="red")
        result_label.config(text="Ungültige ISBN",  foreground="black", background="red")
        fehler_label.config(text=error)  


root=tk.Tk()
root.title("ISBN-legitimations Prüfer")
root.geometry("800x600")
root.configure(background="grey")


style = ttk.Style()
style.configure(".", foreground="Black", background="grey",font=("Arial", 12)) 

first_frame=ttk.Frame(root)
first_frame.pack(pady=20)


search_entry= ttk.Entry(first_frame,width=70,)
search_entry.bind('<KeyRelease>', lambda event: fun())
start_lable=ttk.Label(first_frame,text="Gib die zu prüfende ISBN-Nummer ein:")
strat_button=ttk.Button(first_frame, command=run, text="Prüfen")

start_lable.pack(side="left")
search_entry.pack(side="left")
strat_button.pack(side="right")

result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

fehler_label = ttk.Label(root, text="", font=("Arial", 14))
fehler_label.pack(pady=20)

root.bind('<Return>',lambda event: run())

root.mainloop()
