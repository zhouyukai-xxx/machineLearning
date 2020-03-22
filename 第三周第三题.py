import numpy as np
import math

x0 = np.ones(10)
# x0 = [1,1,1,1,1,1,1,1,1,1]
x1 = np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
x2 = np.array([2,3,4,2,3,4,2,4,1,3])
y= np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,129.44,55.25,104.84])
X= np.stack((x0,x1,x2),axis=1)
Y= y.reshape(10,1)
print(X)
print(Y)
X = np.mat(X)
Y = np.mat(Y)
W =(X.T*X).I*X.T*Y
print(W)
