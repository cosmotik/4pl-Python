from tkinter import *

window = Tk()
window.geometry("550x600")
window.title('Registration form')

title = Label(window, text="Registration form", width=20, font=("bold", 20))
title.place(x=90, y=60)


def exit_window():
    window.destroy()


def submit():
    screen = Frame()
    screen.place(x=0, y=0, width=500, height=530)
    reg_complete = Label(window, text="Registration Done!!", width=30, height=12, font=("bold", 22))
    reg_complete.pack(fill=X)
    button = Button(window, text='ok', width=20, command=exit_window).place(x=165, y=280)


Fullname = Label(window, text="FullName", width=20, font=("bold", 12))
Fullname.place(x=70, y=130)
entry_for_Fullname = Entry(window, width=23)
entry_for_Fullname.place(x=240, y=130)

Username = Label(window, text="Username", width=20, font=("bold", 12))
Username.place(x=68, y=180)
entry_for_Username = Entry(window, width=23)
entry_for_Username.place(x=240, y=180)

Email = Label(window, text="Email Id", width=20, font=("bold", 12))
Email.place(x=70, y=230)
entry_for_Email_Id = Entry(window, width=23)
entry_for_Email_Id.place(x=240, y=232)

Password = Label(window, text="Password", width=20, font=('bold', 12))
Password.place(x=75, y=330)
entry_for_Password = Entry(window, show="*", width=23)
entry_for_Password.place(x=240, y=332)

Confirm = Label(window, text="Confirm Password", width=18, font=('bold', 12))
Confirm.place(x=60, y=380)
entry_for_Confirm_Password = Entry(window, width=23)
entry_for_Confirm_Password.place(x=240, y=382)

check_label = Label(window, text=" ", width=20, font=('bold', 10))
check_label.place(x=200, y=300)

Button(window, text='Submit', width=16, command=submit).place(x=213, y=420)

if Button:
    with open("account.txt") as file:
        data = file.read()
        data = data.split("\n")

def clear_all():
    entry_for_Fullname.delete(0, END)
    entry_for_Username.delete(0, END)
    entry_for_Email_Id.delete(0, END)
    entry_for_Password.delete(0, END)
    entry_for_Confirm_Password.delete(0, END)


button_for_clear_all = Button(window, text='Clear All', width=16, command=clear_all).place(x=213, y=450)

button_for_exit = Button(window, text="Exit", width=16, command=exit).place(x=213, y=480)

window.mainloop()
