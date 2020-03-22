import numpy as np
import math
from numpy import *

np.random.seed(612)
a=np.random.random(size=1000)
b=int(input("请输入一个1-100的数:"))
print("序号  索引值  随机数")
i=1
t=1
for sum in a:
    if t%b == 0:
        print(str(i)+"  "+str(t)+"  "+str(sum))
        i=i+1
    t=t+1
        

