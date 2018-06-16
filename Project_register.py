#torquepakshpandey  pvt limited

from tkinter import TK,stringVar,ttk
from tkinter import *
from time import *

root=TK()
root.title("Attendance register ")
root.geometry('1350*650+0+0')
root.configure(background='black')

#-------------frames-------------------------------------------------------------------------

LeftMayframe=frame(root,width=1000,height=650,bd=8,relif="rasie")
LeftMayframe.pack(side=LEFT)
RightMayframe=frame(root,width=1000,height=650,bd=8,relif="rasie")
RightMayframe.pack(side=RIGHT)


LeftMayframe1=frame(LeftMayframe ,width=1000,height=100,bd=8,relif="rasie")
LeftMayframe1.pack(side=TOP)
LeftMayframe2=frame(LeftMayframe ,width=1000,height=550,bd=8,relif="rasie")
LeftMayframe2.pack(side=TOP)

RightMayframe1=frame(RightMayframe ,width=1000,height=350,bd=8,relif="rasie")
RightMayframe1.pack(side=TOP)
RightMayframe1=frame(RightMayframe ,width=1000,height=350,bd=8,relif="rasie")
RightMayframe1.pack(side=TOP)
#--------------------------------------------------------------------------------------------------

cont1=convas(RightMayframe2,width=350,height=425,bg="black")
cont1.grid(row=0,column=0)
image5=PhotoImage(file="school.png")
cont1.create_image(200,200,image=image5)

#--------------------------------------------------------------------------------------------------

cont= canvas(RightMayframe1,width=350,height=215)
cont.grid(row=0,column=0)
image1=photoImage(file="imag2.png")
image=cont.create_image(200,200,image=image1)

def pic1():
         image=cont.create_image(200,200,image=image1)
 image2=photoImage(file="img3.png")


def pic2():
    image = cont.create_image(200, 200, image=image2)


image3 = photoImage(file="img3.png")


def pic3():
    image = cont.create_image(200, 200, image=image3)


image4 = photoImage(file="img3.png")



def pic4():
    image = cont.create_image(200, 200, image=image4)


image2 = photoImage(file="img3.png")

#--------------variables--------------------------------------------------------------------------
dateoforder=stringVar()
value0=stringVar()
value1=stringVar()
value2=stringVar()
value3=stringVar()
value4=stringVar()
value5=stringVar()
value6=stringVar()
value7=stringVar()
value8=stringVar()
value9=stringVar()
value10=stringVar()
value11=stringVar()
value12=stringVar()

#------------------fillup combobox--------------------------------------------------------------------
def Mark_register():
    if value0.get()=="/":
        value1.set("/")
        value1.set("/")
        value2.set("/")
        value3.set("/")
        value4.set("/")
        value5.set("/")
        value6.set("/")
        value7.set("/")
        value8.set("/")
        value9.set("/")
        value10.set("/")
        value11.set("/")
        value12.set("/")
    elif value0.get()=="0":
        value1.set("0")
        value1.set("0")
        value2.set("0")
        value3.set("0")
        value4.set("0")
        value5.set("0")
        value6.set("0")
        value7.set("0")
        value8.set("0")
        value9.set("0")
        value10.set("0")
        value11.set("0")
        value12.set("0")
    elif value0.get()=="S":
         value1.set("S")
         value1.set("S")
         value2.set("S")
         value3.set("S")
         value4.set("S")
         value5.set("S")
         value6.set("S")
         value7.set("S")
         value8.set("S")
         value9.set("S")
         value10.set("S")
         value11.set("S")
         value12.set("S")
    elif value0.get()=="A":
        value1.set("A")
        value1.set("A")
        value2.set("A")
        value3.set("A")
        value4.set("A")
        value5.set("A")
        value6.set("A")
        value7.set("A")
        value8.set("A")
        value9.set("A")
        value10.set("A")
        value11.set("A")
        value12.set("A")
    elif value0.get()=="L":
         value1.set("L")
         value1.set("L")
         value2.set("L")
         value3.set("L")
         value4.set("L")
         value5.set("L")
         value6.set("L")
         value7.set("L")
         value8.set("L")
         value9.set("L")
         value10.set("L")
         value11.set("L")
         value12.set("L")
    elif value0.get()==" ":
        value1.set(" ")
        value1.set(" ")
        value2.set(" ")
        value3.set(" ")
        value4.set(" ")
        value5.set(" ")
        value6.set(" ")
        value7.set(" ")
        value8.set(" ")
        value9.set(" ")
        value10.set(" ")
        value11.set(" ")
        value12.set(" ")
#-------------------------------Reset------------------------------------------

def reset():
    value0.set("")
    value1.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")
    value11.set("")
    value12 .set("")

#----------------------Exit---------------------------------------
def qExit():
    qExit=messagebox.askyesno("Exit system","do you want to quit")
    if qExit>0:
        root.distroy
        return

#----------date-----------------------------------------------------------------------------------------------------
DateofOrder.set(time.strft("%d/%m/%y"))


#--------Leftmayfeame1--------------------------------------------------------------------------------------------------//

lb1No=label(LeftMayframe1,font=('arial',10,'bold'),text="No.",bd=16)
lb1No.grid(row=0,colomn=0,sticky=W)
lb1StudentNo=label(LeftMayframe1,font=('arial',10,'bold'),text="studentNo.",bd=16)
lb1studentNo.grid(row=0,colomn=1,sticky=W)
lb1StudentName=label(LeftMayframe1,font=('arial',10,'bold'),text="studentName.",bd=16)
lb1StudentName.grid(row=0,colomn=2,sticky=W)
lb1coursecode=label(LeftMayframe1,font=('arial',10,'bold'),text="courseCode.",bd=16)
lb1courseCode.grid(row=0,colomn=3,sticky=W)

box=ttk.combobox(LeftMayframe1,textvarible=value0,state='readonly')
box=['values']=(' ','/','L','O','A','S')
box.current(0)
box.grid(row=0,column=4)

btnFill=button(LeftMayframe ,text='Fill',padx=2,pady=2,bd=2 ,fg='black',font=('arial',10,'bold'),width=12,height=1,command=Mark_register).grid(row=0,column=5)

btnRest=button(LeftMayframe ,text='Rest',padx=2,pady=2,bd ,fg='black',font=('arial',10,'bold'),width=12,height=1,command=Rest).grid(row=0,column=6)

btnExit=button(LeftMayframe ,text='Exit',padx=2,pady=2,bd ,fg='black',font=('arial',10,'bold'),width=12,height=1,command=qExit).grid(row=0,column=7)

lb1Dateoforder=Label(LeftMayframe1,font=('arial',10,'bold'),TextVariable=DateofOrder,padx=2,pady=2,bd=2,fg='black',bg='white',relif='sunken')

Lb1DateofOrder.grid(row=0,column=8,sticky=W)

#--------Leftmayfeame2 row1----------------------------------------------------------------------------------------------///

lb1No=label(LeftMayframe1,font=('arial',10,'bold'),text="No.",bd=16)
lb1No.grid(row=0,colomn=0,sticky=W)

lb1Student_No=label(LeftMayframe1,font=('arial',10,'bold'),text="1232",padx=2,
  pady=2,bd=2,fg="black",width=18)
lb1student_No.grid(row=0,colomn=1,sticky=W)
lb1Student_Name=label(LeftMayframe1,font=('arial',10,'bold'),text="1005",padx=2,
  pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=0,colomn=2,sticky=W)
lb1course_Code=label(LeftMayframe1,font=('arial',10,'bold'),text="courseCode.",bd=16)
lb1course_Code.grid(row=0,colomn=3,sticky=W)

box=ttk.combobox(LeftMayframe2,textvarible=value1,state='readonly')
box=['value']=(' ','/','L','O','S','A')
box.current(0)
box.grid(row=0,column=4)

btnspace=button(LeftMayframe ,text=' ',padx=2,pady=2,bd=2 ,fg='black',font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=0,column=5)

btnspace=button(LeftMayframe ,text=' ',padx=2,pady=2,bd ,fg='black',font=('arial',10,'bold'),width=12,height=1,command=pic3).grid(row=0,column=6)

btnspace=button(LeftMayframe ,text=' ',padx=2,pady=2,bd ,fg='black',font=('arial',10,'bold'),width=12,height=1,command=pic2).grid(row=0,column=7)

btnspace=button(LeftMayframe ,text=' ',padx=2,pady=2,bd ,fg='black',font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=0,column=8)

#--------Leftmayfeame1 row2--------------------------------------------------------------------------------------------//


lb1No=label(LeftMayframe1,font=('arial',10,'bold'),text="2",bd=16)
lb1No.grid(row=1,colomn=0,sticky=W)

lb1Student_No_1=label(LeftMayframe1,font=('arial',10,'bold'),text="1432",padx=2,
   pady=2,bd=2,fg="black",width=18)
lb1student_No_1.grid(row=0,colomn=1,sticky=W)
lb1Student_Name=label(LeftMayframe1,font=('arial',10,'bold'),text="oshodi wales",padx=2,
   pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=0,colomn=2,sticky=W)
lb1course_Code=label(LeftMayframe1,font=('arial',10,'bold'),text="1005",bd=16)
lb1course_Code.grid(row=0,colomn=3,sticky=W)

box=ttk.combobox(LeftMayframe2,textvarible=value2,state='readonly')
box=['value']=(' ','/','L','O','S','A')
box.current(0)
box.grid(row=1,column=4)

btnspace=button(LeftMayframe2 ,text=' ',padx=2,pady=2,bd=2 ,fg='black',font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=0,column=5)

btnspace=button(LeftMayframe2 ,text=' ',padx=2,pady=2,bd ,fg='black',font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=0,column=6)

btnspace=button(LeftMayframe2 ,text=' ',padx=2,pady=2,bd ,fg='black',font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=0,column=7)

btnspace=button(LeftMayframe2 ,text=' ',padx=2,pady=2,bd ,fg='black',font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=0,column=8)


#as same we create the number of students by row by row
#till the 12 row and we need to change the (no,student No,student name ,course code rest all are same
# for row3 textvariable is value3 as same till 12

#---------leftmayframe row3--------------------------------------------------------------------------------------------------------------/////

lb1No=label(LeftMayframe1,font=('arial',10,'bold'),text="3",bd=16)
lb1No.grid(row=2,colomn=0,sticky=W)

lb1Student_No_1=label(LeftMayframe2,font=('arial',10,'bold'),text='2548',padx=2,
   pady=2,bd=2,fg="black",width=18)
lb1student_No_1.grid(row=0,colomn=1,sticky=W)
lb1Student_Name=label(LeftMayframe2,font=('arial',10,'bold'),text='sally monu',padx=2,
   pady=2,bd=2,fg="black",width=12)
lb1Student_Name.grid(row=0,colomn=2,sticky=W)
lb1course_Code=label(LeftMayframe2,font=('arial',10,'bold'),text='1005',bd=16)
lb1course_Code.grid(row=0,colomn=3,sticky=W)

box=ttk.combobox(LeftMayframe2,textvarible=value2,state='readonly')
box=['value']=(' ','/','L','O','S','A')
box.current(0)
box.grid(row=1,column=4)

btnspace=button(LeftMayframe2 ,text=' ',padx=2,pady=2,bd=2 ,fg='black',font=('arial',10,'bold'),width=12,height=1,command=pic3).grid(row=0,column=5)

btnspace=button(LeftMayframe2 ,text=' ',padx=2,pady=2,bd ,fg='black',font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=0,column=6)

btnspace=button(LeftMayframe2 ,text=' ',padx=2,pady=2,bd ,fg='black',font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=0,column=7)

btnspace=button(LeftMayframe2 ,text=' ',padx=2,pady=2,bd ,fg='black',font=('arial',10,'bold'),width=11,height=1,command=pic1).grid(row=0,column=8)


