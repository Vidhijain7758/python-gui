from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button1", fg="red")
button2 = Button(topFrame, text="Button2", fg="blue")
button3 = Button(topFrame, text="Button3", fg="green")
button4 = Button(topFrame, text="Button4", fg="yellow")
button1.pack()
button2.pack()
button3.pack()
button4.pack()
root.mainloop()