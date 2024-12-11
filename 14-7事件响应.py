from tkinter import*
def show1(event):
    ib.configure(text="左键")
def show3(event):
    ib.configure(text="右键")
root=Tk()
root.title("按键实验1")
root.geometry("200x200")


ib=Label(root,text="")
ib.pack()
btn=Button(root,text="按钮")
btn.bind("<ButtonPress-1>",show1)

btn.bind("<ButtonPress-3>",show3)

btn.focus_set()
btn.pack()


root.mainloop()
