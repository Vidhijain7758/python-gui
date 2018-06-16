from tkinter import *

root = Tk()

photo = PhotoImage(file="original.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()