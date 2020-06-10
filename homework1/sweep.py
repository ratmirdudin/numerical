import numpy as np
import scipy.linalg as sl
import time
import random
import matplotlib.pyplot as plt

def randd(n):
  A = np.zeros((n, n))
  for a in range(n):
    for b in range(a - 1, a + 2):
      if b == -1:
        A[a][0] = random.random()
        continue
      if b == n:
        break
      A[a][b] = random.random()
  return A

def create_abc(A, n):
  a = np.zeros(n)
  b = np.zeros(n)
  c = np.zeros(n)
  for i in range(n):
    for j in range(i - 1, i + 2):
      if j == i - 1 and j != -1:
        a[i-1] = A[i][j]
      if j == i:
        c[i] = A[i][j]
      if j == i + 1 and j != n:
        b[i + 1] = A[i][j]
  return np.array([b, c, a])


print('Please, input nubmer, where number * 1000 will be sizes of matrix')
size = int(input())
my_time = np.zeros(size)
np_time = np.zeros(size)

for iterator in range(1, size + 1):

  n = iterator * 1000

  A = randd(n)
  f = np.random.rand(n)
  x = np.zeros(n)
  abc = create_abc(A, n)

  start_time = time.time()# Numpy
  X = sl.solve_banded((1, 1), abc, f)
  np_time[iterator-1] = time.time() - start_time


  start_time = time.time()# My

  m = 1;  
  for i in range(1, n):
    m = A[i][i - 1] / A[i - 1][i - 1]
    A[i][i] = A[i][i] - m * A[i - 1][i]
    f[i] = f[i] - m * f[i - 1]

  x[n - 1] = f[n - 1] / A[n - 1][n - 1];
  for i in range(n - 2, -1, -1):
    x[i] = (f[i] - A[i][i + 1] * x[i + 1]) / A[i][i]

  my_time[iterator - 1] = time.time() - start_time


  print('n = ', n)
  print('My time:', my_time[iterator - 1])
  print('Np time:', np_time[iterator - 1])
  print()

plot = np.linspace(1000, 1000 * size, size)
plt.title('Sweep')
plt.plot(plot, np_time, label = 'Numpy time')
plt.plot(plot, my_time, label = 'My time')
plt.legend()
plt.ylabel('Time')
plt.xlabel('Matrix size')
plt.show()