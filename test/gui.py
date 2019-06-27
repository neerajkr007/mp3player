import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, height=300, width=300)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relheight=0.5, relwidth=0.5)

button = tk.Button(root, text='Test button', fg='blue')
button.pack()

root.mainloop()
