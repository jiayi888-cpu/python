from tkinter import*
root = Tk()
root.title("计算器")
root.geometry("1100x600")

def num(number):
    first_num=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(first_num)+str(number))
def calculate():
    result = eval(entry.get())
    s=(entry.get(),"=",result)
    tet.insert(END,s)
    entry.delete(0,END)       
    entry.insert(END,str(result))
def clear():
    entry.delete(0,END)

bu7=Button(root,text=7,width=2,font=("Arial",30),command=lambda:num(7))
bu8=Button(root,text=8,width=2,font=("Arial",30),command=lambda:num(8))
bu9=Button(root,text=9,width=2,font=("Arial",30),command=lambda:num(9))
bu4=Button(root,text=4,width=2,font=("Arial",30),command=lambda:num(4))
bu5=Button(root,text=5,width=2,font=("Arial",30),command=lambda:num(5))
bu6=Button(root,text=6,width=2,font=("Arial",30),command=lambda:num(6))
bu1=Button(root,text=1,width=2,font=("Arial",30),command=lambda:num(1))
bu2=Button(root,text=2,width=2,font=("Arial",30),command=lambda:num(2))
bu3=Button(root,text=3,width=2,font=("Arial",30),command=lambda:num(3))
bu0=Button(root,text=0,width=2,font=("Arial",30),command=lambda:num(0))
bupoint=Button(root,text=".",width=2,font=("Arial",30),command=lambda:num("."))
bue=Button(root,text="=",width=2,font=("Arial",30),command=lambda:calculate())
buadd=Button(root,text="+",width=2,font=("Arial",30),command=lambda:num("+"))
bujian=Button(root,text="-",width=2,font=("Arial",30),command=lambda:num("-"))
bucheng=Button(root,text="*",width=2,font=("Arial",30),command=lambda:num("*"))
budiv=Button(root,text="/",width=2,font=("Arial",30),command=lambda:num("/"))
buclear=Button(root,text="C",width=2,font=("Arial",30),command=lambda:clear())

bu7.place(x=10,y=100)
bu8.place(x=70,y=100)
bu9.place(x=130,y=100)
bu4.place(x=10,y=185)
bu5.place(x=70,y=185)
bu6.place(x=130,y=185)
bu1.place(x=10,y=270)
bu2.place(x=70,y=270)
bu3.place(x=130,y=270)
bu0.place(x=10,y=355)
bupoint.place(x=70,y=355)
bue.place(x=130,y=355)
buadd.place(x=190,y=355)
bujian.place(x=190,y=270)
bucheng.place(x=190,y=185)
budiv.place(x=190,y=100)
buclear.place(x=10,y=440)

entry=Entry(root,fg="green",width=10,font=("Arial",31))
entry.place(x=10,y=30)
tet=Text(root)
tet.pack()
root.mainloop()
