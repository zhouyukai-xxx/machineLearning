import numpy as np
import math
from numpy import *

np.random.seed(612)
a=np.random.random(size=1000)
b=int(input("������һ��1-100����:"))
print("���  ����ֵ  �����")
i=1
t=1
for sum in a:
    if t%b == 0:
        print(str(i)+"  "+str(t)+"  "+str(sum))
        i=i+1
    t=t+1
        

