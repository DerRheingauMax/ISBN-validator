import tkinter as tk
from tkinter import ttk

import isbn_validator as isbn_validator
neutral_color = "grey"
fail_color = "red"
succses_color = "green"

def change_backgroundcolor(color):
    root.config(background=color)
    result_label.config(background=color)
    style.configure("Transparent.TFrame", background=color)
    instruction_label.config(background=color)
    error_label.config(background=color)


def reset_screen():
    change_backgroundcolor(neutral_color)
    result_label.config(text="", foreground=succses_color) 
    error_label.config(text="", foreground=fail_color)

def check_isbn():
    result, error =isbn_validator.validate_isbn(isbn_entry.get())

    if result:
        change_backgroundcolor(succses_color)
        result_label.config(text=" Gültige ISBN", foreground="black") 
    else:
        change_backgroundcolor(fail_color)
        result_label.config(text="Ungültige ISBN",  foreground="black")
        error_label.config(text=error, foreground= "black")  


root=tk.Tk()
root.title("ISBN-legitimations Prüfer")
root.geometry("800x600")
root.configure(background=neutral_color)


style = ttk.Style()
style.configure(".", foreground="Black", background=neutral_color,font=("Arial", 12)) 

first_frame=ttk.Frame(root,style="Transparent.TFrame")
second_frame = ttk.Frame(root,style="Transparent.TFrame")
style = ttk.Style()
style.configure("Transparent.TFrame", background=neutral_color) 

isbn_entry= ttk.Entry(first_frame,width=70,)
isbn_entry.bind('<KeyPress>', lambda event: reset_screen())
instruction_label=ttk.Label(first_frame,text="Gib die zu prüfende ISBN-Nummer ein:")
check_button=ttk.Button(first_frame, command=check_isbn, text="Prüfen")



error_label = ttk.Label(second_frame, text="", font=("Arial", 14))

result_label = ttk.Label(second_frame, text="", font=("Arial", 14))


root.bind('<Return>',lambda event: check_isbn())
first_frame.configure()

#root
first_frame.place(relx=0.5, rely=0.3, anchor="center")
second_frame.place(relx=0.5, rely=0.5, anchor="center")
#first_frame
instruction_label.pack(pady=15)
isbn_entry.pack()
check_button.pack(pady=15)
#second_frame
result_label.pack(pady=20)
error_label.pack()



root.mainloop()
