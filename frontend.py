import tkinter as tk
from tkinter import ttk

import isbn_validator as isbn_validator


def fun():
    result_label.config(text="", foreground="green", background="grey") 
    root.configure(background="grey")
    error_label.config(text="", foreground="red",background="grey")
    style.configure("Transparent.TFrame", background="grey")
    instruction_label.config(background="grey")

def run():
    result, error =isbn_validator.validate_isbn(isbn_entry.get())

    if result:
        root.configure(background="grey")
        result_label.config(text=" Gültige ISBN", foreground="green", background="grey") 
        style.configure("Transparent.TFrame", background="grey") 
        instruction_label.config(background="grey")
    else:
        root.configure(background="red")
        instruction_label.config(background="red")
        result_label.config(text="Ungültige ISBN",  foreground="black", background="red")
        error_label.config(text=error, foreground= "black", background= "red")  
        style.configure("Transparent.TFrame", background="red") 


root=tk.Tk()
root.title("ISBN-legitimations Prüfer")
root.geometry("800x600")
root.configure(background="grey")


style = ttk.Style()
style.configure(".", foreground="Black", background="grey",font=("Arial", 12)) 

first_frame=ttk.Frame(root,style="Transparent.TFrame")
style = ttk.Style()
style.configure("Transparent.TFrame", background="grey") 

isbn_entry= ttk.Entry(first_frame,width=70,)
isbn_entry.bind('<KeyPress>', lambda event: fun())
instruction_label=ttk.Label(first_frame,text="Gib die zu prüfende ISBN-Nummer ein:")
check_button=ttk.Button(first_frame, command=run, text="Prüfen")



error_label = ttk.Label(root, text="", font=("Arial", 14))

result_label = ttk.Label(root, text="", font=("Arial", 14))


root.bind('<Return>',lambda event: run())
first_frame.configure()

#root
first_frame.pack(pady=20)
result_label.place(relx=0.5, rely=0.5, anchor="center")
error_label.pack(pady=20)
#first_frame
instruction_label.pack()
isbn_entry.pack()
check_button.pack(pady=15)



root.mainloop()
