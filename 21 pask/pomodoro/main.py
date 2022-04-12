from tkinter import *
import math

work = 25
short_break = 5
long_break = 30
reps = 0
timer = None

window = Tk()
window.title("Pomodoro")
window.config(padx=300, pady=100, bg="green")
title_label = Label(text="Timer", fg="black", bg="green", font=("Courier", 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=220, bg="green", highlightthickness=0)
timer_text = canvas.create_text(95, 60, text="00:00", fill="white", font=("Courier", 46, "bold"))
canvas.grid(column=1, row=1)
#pomodoro_img = PhotoImage(file="pomodoro.jpg")
#canvas.create_image(100, 112, image=pomodoro_img)


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


def start_timer():
    global reps
    reps += 1
    work_sec = work * 60
    short_break_sec = short_break * 60
    long_break_sec = long_break * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long_Break", fg="black")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg="black")
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg="black")


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    global reps
    reps = 0


start_button = Button(text="Start", highlightthickness=10, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=10, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
