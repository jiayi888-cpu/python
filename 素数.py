s=int(input("请输入一个整数；"))
if s<2:
    print("这个数不是素数！")
else:
     for i in range(2,s):
        if s%i==0:
            print("这个数不是素数！")
            break
     else:
        print("这个数是素数")
                    
