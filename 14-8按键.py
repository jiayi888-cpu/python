from tkinter import*
root=Tk()
root.title=("按键实验")
root.geometry("200x200")

def show(event):
    s=event.keysym
    Ib.config(text=s)
Ib=Label(root,text="请按键",font=("黑体",48))
Ib.bind("<Key>",show)
Ib.focus_set()
Ib.pack()
root.mainloop()
