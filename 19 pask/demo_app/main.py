from tkinter import *

window = Tk()
window.title("Demo")
window.minsize(width=500, height=500)


def button_clicked():
    print("Clicked")


def spinbox_used():
    print(spinbox.get())


def scale_used(value):
    print(value)


def checkbox_used():
    print(check_state.get())


def radio_used():
    print(radio_state.get())


def listbox_used(event):
    print(list_box.get(list_box.curselection()))


label = Label(text="Label")
label.pack()

button = Button(text="Button", command=button_clicked)
button.pack()

entry = Entry(width=30)
entry.insert(END, string="Text_inserted")
entry.pack()

text = Text(height=5, width=30)
text.pack()

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

check_state = IntVar()
check_button = Checkbutton(text="Is on?", variable=check_state, command=checkbox_used)
check_button.pack()

radio_state = IntVar()
radio_button_1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio_button_2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radio_button_1.pack()
radio_button_2.pack()

list_box = Listbox(height=4)
colors = ["red", "green", "blue"]
for item in colors:
    list_box.insert(colors.index(item), item)

list_box.bind("<<ListboxSelect>>", listbox_used)
list_box.pack()

window.mainloop()
