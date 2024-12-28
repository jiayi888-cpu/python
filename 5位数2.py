a=input("输入一个五位数：")
if len(a)!=5:
    print("不是5位")
else:
    eval(a)
    print("千位数是：{},个位数是：{}".format(a[-3],a[-1]))
