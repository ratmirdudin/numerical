import numpy as np
import matplotlib.pyplot as plt
from math import *

def sweep(n, a, b, c, f):
  x = np.zeros(n)
  alpha = np.zeros(n + 1)
  beta = np.zeros(n + 1)
  a[0] = 0
  c[n -  1] = 0
  alpha[0] = 0
  beta[0] = 0
  for i in range(n):  
    d = a[i] * alpha[i] + b[i]
    alpha[i + 1] = -c[i] / d
    beta [i + 1] = (f[i] - (a[i] * beta[i])) / (d)
  x[n - 1] = beta[n]
  for i in range(n - 2, -1, -1):
    x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
  return x

def generateSpline(x, y):
  n = len(x) - 1
  h = (x[n] - x[0]) / n

  a = np.array([0] + [1] * (n - 1) + [0])
  b = np.array([1] + [4] * (n - 1) + [1])
  c = np.array([0] + [1] * (n - 1) + [0])
  f = np.zeros(n + 1)
  for i in range(1, n):
    f[i] = 3 * (y[i - 1] - 2 * y[i] + y[i + 1]) / h**2

  s = sweep(n + 1, a, b, c, f)

  #print('a = ', a)
  #print('b = ', b)
  #print('c = ', c)
  #print('f = ', f)
  #print('s = ', s, '\n')
  
  A = np.zeros(n + 1)
  B = np.zeros(n + 1)
  C = np.zeros(n + 1)
  D = np.zeros(n + 1)

  for i in range(n):
    B[i] = s[i]
    D[i] = y[i]
  for i in range(n):
    A[i] = (B[i + 1] - B[i]) / (3 * h)
    C[i] = ((y[i + 1] - y[i]) / h) - ((B[i + 1] + 2 * B[i]) * h) / 3
  return A, B, C, D

def spline(t, m, x, A, B, C, D):
  f = np.zeros(m)
  for j in range(m):
    for i in range(n - 1):
      if t[j] < x[0]:
        f[j] = A[0] * (t[j] - x[0])**3 + B[0] * (t[j] - x[0])**2 + C[0] * (t[j] - x[0]) + D[0]
      if t[j] >= x[n - 1]:
        f[j] = A[n - 2]*(t[j] - x[n - 2])**3 + B[n - 2] * (t[j] - x[n - 2])**2 + C[n - 2]*(t[j] - x[n - 2]) + D[n - 2]
      if x[i] < t[j] <= x[i + 1]:
        f[j] = A[i] * (t[j] - x[i])**3 + B[i]*(t[j] - x[i])**2 + C[i] * (t[j] - x[i]) + D[i]
    test_y.write(str(f[j]) + ' ')
  return f

train_x = open('data3/train.dat', 'r')
train_y = open('data3/train.ans', 'r')
test_x = open('data3/test.dat', 'r')
test_y = open('data3/test.ans', 'w')

x = [float(i) for i in train_x.readline().split()]
y = [float(i) for i in train_y.readline().split()]
z = [float(i) for i in  test_x.readline().split()]
n = len(x)
m = len(z)


A, B, C, D = generateSpline(x, y)

f = spline(z, m, x, A, B, C, D)


print('Count train = ', n)
print('x = ', x)
print('y = ', y)
print('Count of test = ', m)
print('z = ', z)
print('f = ', f)

min_xz = min(np.min(x), np.min(z))
max_xz = max(np.max(x), np.max(z))

x_plt = np.linspace(min_xz , max_xz, 50)
y_plt = spline(x_plt, len(x_plt), x, A, B, C, D)

train_x.close()
train_y.close()
test_x.close()
test_y.close()

plt.plot(x_plt, y_plt, 'b', label = 'spline')
plt.plot(x, y, 'o', label = 'train')
plt.plot(z, f, 'r*', label = 'test')
plt.ylabel('y(x), f(z)')
plt.xlabel('x, z')
plt.legend()
plt.grid()
plt.show()