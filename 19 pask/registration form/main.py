from tkinter import *

window = Tk()
window.minsize(width=500, height=500)
window.title("Registration Form")

label_name = Label(window, text="Name", width=20, font=("bold", 10))
label_name.place(x=70, y=130)
entry_name = Entry(window)
entry_name.place(x=240, y=130)

label_email = Label(window, text="Email", width=20, font=("bold", 10))
label_email.place(x=70, y=180)
entry_email = Entry(window)
entry_email.place(x=240, y=180)

label_password = Label(window, text="Password", width=20, font=("bold", 10))
label_password.place(x=70, y=230)
entry_password = Entry(window)
entry_password.place(x=240, y=230)

label_rpassword = Label(window, text="Repeat your password:", width=20, font=("bold", 10))
label_rpassword.place(x=70, y=280)
entry_rpassword = Entry(window)
entry_rpassword.place(x=240, y=280)

Button(window, text='Submit', width=20).place(x=180, y=380)

window.mainloop()