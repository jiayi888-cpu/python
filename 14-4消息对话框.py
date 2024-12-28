from tkinter import*
import tkinter.messagebox
root=Tk()
def xz():
    answer=tkinter.messagebox.askokcancel("请选择","请选择确定或取消")
    if answer:
        Ib.config(text="已确认")
    else:
        Ib.config(text="已取消")
Ib=Label(root,text="")
Ib.pack()
btn=Button(root,text="弹出对话框",command=xz)
btn.pack()
root.mainloop()
