from tkinter import*
def run1():
    a=eval(inp1.get())
    b=eval(inp2.get())
    s="{:.2f}+{:.2f}={:.2f}\n".format(a,b,a+b)
    txt.insert(END,s)
    inp1.delete(0,END)
    inp2.delete(0,END)
root=Tk()
root.title("加法器")
root.geometry("500x500")
ib1=Label(root,text="请输入两个数")
ib1.pack()
inp1=Entry(root)
inp1.pack()
inp2=Entry(root)
inp2.pack()

btn1=Button(root,text="+",command=run1)
btn1.pack()
txt=Text(root)
txt.pack()
root.mainloop()
              
