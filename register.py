from tkinter import Tk, StringVar, ttk
from tkinter import *
import time
import datetime

root = Tk()
root.title("Attendance Register")
root.geometry('1350*650+0+0')
root.configure(background='black')

LeftMayFrame = Frame(root, width=1000, height=650, bd=8, relief="raise")
LeftMayFrame.pack(side=LEFT)
RightMayFrame = Frame(root, width=550, height=650, bd=8, relief="raise")
RightMayFrame.pack(side=RIGHT)

LeftMayFrame1 = Frame(LeftMayFrame, width=1000, height=100, bd=8, relief="raise")
LeftMayFrame1.pack(side=TOP)
LeftMayFrame2 = Frame(LeftMayFrame, width=1000, height=100, bd=8, relief="raise")
LeftMayFrame2.pack(side=TOP)

RightMayFrame1 = Frame(RightMayFrame, width=350, height=215, bd=8, relief="raise")
RightMayFrame1.pack(side=TOP)
RightMayFrame2 = Frame(RightMayFrame, width=350, height=215, bd=8, relief="raise")
RightMayFrame2.pack(side=TOP)

#------------------Variables---------------

DateOfOrder = StringVar()
value0 = StringVar()
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()
value6 = StringVar()
value7 = StringVar()
value8 = StringVar()
value9 = StringVar()
value10 = StringVar()
value11 = StringVar()
value12 = StringVar()

#-------------------------COMPONENTS-----------------------
DateOfOrder.set(time.strftime("%d/%m/%Y"))

root.mainloop()
