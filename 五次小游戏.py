import random
points=0
for i in range(5):
    a=random.randint(0,10)
    b=random.randint(0,10)
    print("请计算两个数字之和：",a,b)
    c=int(input())
    if c==a+b:
        points+=1
if points>=4:
    print("成功")
else:
    print("失败")      

   
