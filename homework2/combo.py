import numpy as np
import time 
import matplotlib.pyplot as plt
from math import *

def jacobi(n, A, f, x):
  xnew = np.zeros(n)
  for i in range(n):
    summ = 0
    for j in range(i):
      summ = summ + A[i][j] * x[j]
    for j in range(i + 1, n):
      summ = summ + A[i][j] * x[j]
    xnew[i] = (f[i] - summ) / A[i][i]
  return xnew

def jacobi_solve(n, A, f):
  xnew = np.zeros(n)
  while True:
    x = np.array(xnew)
    xnew = jacobi(n, A, f, x)
    if diff(n, x, xnew) < eps:
      break
  return xnew

def zeidel(n, A, f, x):
  xnew = np.zeros(n)
  for i in range(n):
    summ = 0
    for j in range(i):
      summ = summ + A[i][j] * xnew[j]
    for j in range(i + 1, n):
      summ = summ + A[i][j] * x[j]
    xnew[i] = (f[i] - summ) / A[i][i]
  return xnew

def zeidel_solve(n, A, f):
  xnew = np.zeros(n)
  while True:
    x = np.array(xnew)
    xnew = zeidel(n, A, f, x)
    if diff(n, x, xnew) < eps:
      break
  return xnew

def diff(n, x, y):
  summ = 0
  for i in range(n):
    summ = summ + (x[i] - y[i]) ** 2
  return sqrt(summ)


eps = 0.1
print('Please, input k, where k * 100 will be sizes of matrix')
size = int(input())
jj_time = np.zeros(size)
zz_time = np.zeros(size)
np_time = np.zeros(size)

for iterator in range(1, size + 1):

  n = iterator * 100
  A = np.random.rand(n, n)
  f = np.random.rand(n)

  summ = np.sum(np.abs(A), axis = 1)
  for i in range(n):
    A[i][i] = A[i][i] + summ[i]

  start = time.time()# Numpy
  X = np.linalg.solve(A, f)
  np_time[iterator - 1] = time.time() - start

  start = time.time()# My Zeidel
  x1 = zeidel_solve(n, A, f)
  zz_time[iterator - 1] = time.time() - start

  start = time.time()# My Jacobi
  x2 = jacobi_solve(n, A, f)
  jj_time[iterator - 1] = time.time() - start

  print('n = ', n)
  print('My Zeidel time:', zz_time[iterator - 1])
  print('My Jacobi time:', jj_time[iterator - 1])
  print('Np time:', np_time[iterator - 1])
  print()

plot = np.linspace(100, size * 100, size)
plt.title('Jacobi and Zeidel')
plt.plot(plot, np_time, label = 'Numpy time')
plt.plot(plot, jj_time, label = 'My Jacobi time')
plt.plot(plot, zz_time, label = 'My Zeidel time')
plt.legend()
plt.ylabel('Time')
plt.xlabel('Matrix size')
plt.show()