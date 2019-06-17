# python clock with TK
from tkinter import *
import tkinter as tk
import time

WIDTH = 500
HEIGHT = 500
pi = 3.141592653

root = tk.Tk()

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
root.title('Digital Clock')


def text():
    canvas.delete(ALL)
    canvas.create_text(WIDTH / 2, HEIGHT / 8, fill='green',
                       font="Times 60 italic bold", text=(str(time.strftime('%H:%M:%S'))))
    canvas.update()
    canvas.after(200, text)
    canvas.pack(fill='both', expand=True)


def clock_frame():
    HOUR = int(time.strftime('%H'))
    MINUTES = int(time.strftime('%M'))
    canvas.create_arc(WIDTH / 2 - 100, HEIGHT / 2 - 100, WIDTH / 2 + 100, HEIGHT / 2 + 100, start=90,
                      extent=-(int(time.strftime('%S'))) / 0.166204, width=6, outline='green', style=tk.ARC)
    canvas.create_arc(WIDTH / 2 - 93, HEIGHT / 2 - 93, WIDTH / 2 + 93, HEIGHT / 2 + 93, start=90,
                      extent=-(int(time.strftime('%M'))) / 0.16713091, width=7, outline='yellow', style=tk.ARC)
    canvas.create_arc(WIDTH / 2 - 87, HEIGHT / 2 - 87, WIDTH / 2 + 87, HEIGHT / 2 + 87, start=91, extent=-(
        int(time.strftime('%H'))) / 0.066481994, width=8, outline='medium blue', style=tk.ARC)
    canvas.pack()
    canvas.update()
    canvas.after(1, clock_frame)


text()
clock_frame()
root.mainloop()
