from tkinter import *

window = Tk()
window.title("My first program")
window.minsize(width=500, height=300)


def submit_form():
    text = name_input.get()
    if len(text) > 0:
        name_label = Label(text=f"Name is {text}", font=("Arial", 14, "bold"))
        name_label.grid(column=1, row=1)
        label.config(text=f"Name submitted")


label = Label(text="Your name:", font=("Arial", 14, "bold"))
label.grid(column=0, row=0)

name_input = Entry(width=15)
name_input.grid(column=0, row=1)

button = Button(text="Submit", command=submit_form)
button.grid(column=0, row=2)

window.mainloop()
