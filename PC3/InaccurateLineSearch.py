import numpy as np
import matplotlib.pyplot as plt

def line_search(f, df, x, alpha, d, eps = 1.0e-8):
  e = 0.3
  n = 1.2
  for i in range(500):
    while(f(x+alpha*d) > f(x)+e*df(x)*alpha):
      alpha = alpha/n
    print("alpha_"+str(i)+" = "+str(alpha))
    xk = x + alpha*d
    print("x_"+str(i)+" = "+str(x))
    if(abs(xk - x) < eps):
      return xk
    x = xk

def f(x):
  return x**2+20*x

def df(x):
  return 2*x+20

x = -20.0
alpha = 1.0
d = 2.0

X = np.arange(-30,30,0.1)
Y = f(X)
plt.plot(X,Y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print(line_search(f,df,x,alpha,d))