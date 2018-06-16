from tkinter import *

root = Tk()

canvas = Canvas(root, width=1350, height=800)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 1250)
redLine = canvas.create_line(0, 100, 200, 1250, fill="red")

# canvas.delete(blackLine)
# canvas.delete(redLine)


root.mainloop()