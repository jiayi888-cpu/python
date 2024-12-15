import tkinter 
import time
def gettime():
    timestr=time.strftime("%H:%M:%S")
    lb.configure(text=timestr)
    root.after(1000,gettime)
root=tkinter.Tk()
root.title("时钟")
lb=tkinter.Label(root,text="",fg="black",font=("黑体",80))
lb.pack()
gettime()
root.mainloop()
