"""测试Grid布局管理器的基本用法，使用面向对象的方式"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)        # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()


    def createWidget(self):
        """通过grid布局实现登录界面"""
        self.label01 = Label(self,text="用户名")
        self.label01.grid(row=0,column=0,pady=10)
        self.entry01 = Entry(self)
        self.entry01.grid(row=0,column=1,pady=10)
        Label(self,text="用户名为手机号",foreground="gray").grid(row=0,column=2)

        Label(self, text="密码").grid(row=1, column=0,pady=10)
        self.entry02 = Entry(self, show="*")
        self.entry02.grid(row=1, column=1,pady=10)

        #EW表示组件在水平方向上拉满该栅格
        Button(self, text="登录",command=self.mylogin).grid(row=2, column=1, sticky=EW)
        Button(self, text="取消", command=root.destroy).grid(row=2, column=2, sticky=E)


    def mylogin(self):
        username = self.entry01.get()
        pwd = self.entry02.get()

        print("去数据库比对用户名和密码！")
        print("用户名："+username)
        print("密码："+pwd)

        if username=="13333333333" and pwd=="123456":
            messagebox.showinfo("景天科技苑学习系统", "登录成功！欢迎开始学习！")
        else:
            messagebox.showinfo("景天科技苑学习系统","登录失败！用户名或密码错误！")



if __name__ == '__main__':
    root = Tk()
    root.geometry("500x120+200+300")
    root.title("用户登录")
    app = Application(master=root)
    root.mainloop()
