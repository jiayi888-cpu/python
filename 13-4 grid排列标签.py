from tkinter import*
root=Tk()
Ibred=Label(root,text="红",fg="red",relief=GROOVE)
Ibred.grid(column=2,row=0)

Ibgreen=Label(root,text="绿",fg="green",relief=GROOVE)
Ibgreen.grid(column=0,row=1)

Ibblack=Label(root,text="黑",fg="black",relief=GROOVE)
Ibblack.grid(column=1,row=1)

Ibblue=Label(root,text="蓝",fg="blue",relief=GROOVE)
Ibblue.grid(column=1,columnspan=2,row=2)
root.title("标签")
root.mainloop()
