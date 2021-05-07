import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=600, height=600, bg='Blanched almond')
canvas1.pack()

def hello():
    label1 = tk.Label(root, text='"Hello Programming World! Python is the best programming language!"\n''- Amena Akter', fg='purple',  font=('times new roman', 14, 'bold', 'italic'))
    canvas1.create_window(300, 300, window=label1)

button1 = tk.Button(text='Click Here', command=hello, bg='Cyan', fg='black' , font=('times new roman', 14, 'bold'))
canvas1.create_window(300, 300, window=button1)

root.mainloop()