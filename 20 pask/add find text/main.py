from tkinter import *

window = Tk()
window.title("Notes")
window.minsize(width=500, height=500)

fram = Frame(window)

Label(fram, text='Text to find:').pack(side=LEFT)

# adding of single line text box
edit = Entry(fram)

edit.pack(side=LEFT, fill=BOTH, expand=1)

button = Button(fram, text='Find')
button.pack(side=RIGHT)
fram.pack(side=TOP)

text = Text(window)

text.insert('1.0', '''Type your text here''')
text.pack(side=BOTTOM)


def find():
    text.tag_remove('found', '1.0', END)

    s = edit.get()
    if s:
        idx = '1.0'
        while 1:
            idx = text.search(s, idx, nocase=1, stopindex=END)
            if not idx:
                break

            lastidx = '%s+%dc' % (idx, len(s))

            text.tag_add('found', idx, lastidx)
            idx = lastidx

        text.tag_config('found', foreground='red')
    edit.focus_set()


button.config(command=find)
window.mainloop()
