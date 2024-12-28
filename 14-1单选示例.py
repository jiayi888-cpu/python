from tkinter import*

def mysel():
    choice=var.get()
    choice_dict={0:"甲",1:"乙",2:"丙"}
    s="您选择了{}".format(choice_dict[choice])
    ib.configure(text=s)

root=Tk()
root.title=("radiobutton")
root.geometry("200x200")

ib=Label(root)
ib.pack()
var=IntVar()
rd1=Radiobutton(root,text="甲",variable=var,value=0,command=mysel)
rd1.pack()
rd2=Radiobutton(root,text="乙",variable=var,value=0,command=mysel)
rd2.pack()
rd3=Radiobutton(root,text="丙",variable=var,value=0,command=mysel)
rd3.pack()
root.mainloop()
