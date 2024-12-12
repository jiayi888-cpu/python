import  matplotlib.pyplot as plt
import numpy as np


if __name__=="__main__":
    x=np.linspace(0,10,100)
    y=4+5*np.sin(6*x)
    linewidth_num=2.0
    xlim_param=[0,10]
    ylim_param=[-2,10]
    xticks_param=np.arange(1,11)
    yticks_param=np.arange(-2,11)
ax=plt.subplot()
ax.plot(x,y,linewidth=linewidth_num)
ax.set(xlim=(xlim_param[0],xlim_param[1]),xticks=xticks_param,ylim=(ylim_param[0],ylim_param[1]),yticks=yticks_param)

plt.show()
