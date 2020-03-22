import numpy as np
import math

x=[64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]
x=np.asarray(x)
y=[62.55,82.42,132.62,73.31,131.05,86.57,85.49,129.44,55.25,104.84]
y=np.asarray(y)
Size=y.size
xavg = np.mean(x)
yavg = np.mean(y)
i=0
j=0
Sum=0
Sam=0
while i<Size:
    Sum = Sum+(x[i]-xavg)*(y[i]-yavg)
    i=i+1
while j<Size:
    Sam = Sam+(x[j]-xavg)*(x[j]-xavg)
    j=j+1
w=Sum/Sam
b=yavg-w*xavg
print("w="+str(w))
print("b="+str(b))

   

       



