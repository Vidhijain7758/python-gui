from tkinter import *

def doNothing():
    print("\nOkk, I won't do nothing!!!")

# def doSomething():
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     sum = a + b
#     print("\nThe Sum is", sum)

root = Tk()

mainMenu = Menu(root)  #-----Showing in Frame-------
# -------Main Menu---------
root.config(menu=mainMenu)
# --------- Main Menu will have File and having Submenus-File, New Project, Now, Exit
subMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing())
subMenu.add_command(label="Now..", command=doNothing())
subMenu.add_separator()
subMenu.add_command(label="Exit..", command=quit())
subMenu.add_separator()

# editMenu = Menu(mainMenu)
# editMenu.add_cascade(label="Arithmetic", menu=editMenu)
# editMenu.add_command(label="Sum", command=doSomething())
# editMenu.add_separator()

root.mainloop()