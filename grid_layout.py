from tkinter import *
root = Tk()

# frame = tk.Frame(root)
# frame.pack()

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Passwd")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

check_btn = Checkbutton(root, text="keep me signIn")
check_btn.grid(columnspan=2)

# button1 = tk.Button(frame, text="Submit", fg="red", command=quit())
# button1.pack()

root.mainloop()