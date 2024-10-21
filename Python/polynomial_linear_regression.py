import time
import numpy as np
import matplotlib.pyplot as plt


path='D:/pycv/lessons/dataset/train.txt'
train_set=np.loadtxt(path)
train_set=train_set[:,[0,1,3]]

X1=train_set[:,0]
Y=train_set[:,1]
print(Y)

X2=X1**2
X3=X1**3
X0=np.ones_like(X1)
X=np.c_[X0,X1,X2,X3]
best_P=np.linalg.pinv(X.T@X)@X.T@Y


X1=X1.reshape(-1)
xline=np.arange(10,2000,1)
X_line0=np.ones_like(xline)

X_line1=xline
X_line2=X_line1**2
X_line3=X_line1**3
X_all=np.c_[X_line0,X_line1,X_line2,X_line3]

H=X_all@best_P
plt.figure(1)
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0,500,0,0.5])
plt.plot(X1,Y,label='fact',color='red')
plt.plot(xline,H,label='hypothesis',color='green')
plt.legend()
plt.show()

                   

            
            
