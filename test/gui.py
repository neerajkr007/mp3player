import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer

root = tk.Tk()
mixer.init()

canvas = tk.Canvas(root, height=300, width=300)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relheight=1, relwidth=1)

menubar = tk.Menu(root)
root.config(menu=menubar)
submenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=submenu)


def file_browser():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)


submenu.add_command(label='open', command=file_browser)


def load_play():
    if mixer.music.get_pos() == -1:
        try:
            mixer.music.load(filename)
            mixer.music.play(0)
        except:
            tkinter.messagebox.showinfo(title='Error', message="Load a file first")
    else:
        mixer.music.unpause()


button = tk.Button(root, text='play', fg='blue', command=load_play)
button.pack()


def pause():
    mixer.music.pause()


button = tk.Button(root, text='pause', fg='blue', command=pause)
button.pack()


def stop():
    mixer.music.stop()


button = tk.Button(root, text='stop', fg='blue', command=stop)
button.pack()


def pos():
    print(mixer.music.get_pos())


button = tk.Button(root, text='pos', fg='blue', command=pos)
button.pack()
# message = tk.Message(frame, text='test_player')
# message.pack()

root.mainloop()
