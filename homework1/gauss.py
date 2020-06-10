import numpy as np
import time
import matplotlib.pyplot as plt

print('Please, input number, where number * 100 will be sizes of matrix')
size = int(input())
np_time = np.zeros(size)
my_time = np.zeros(size)

for iterator in range(1, size + 1):
 
  n = iterator * 100

  A = np.random.rand(n, n)
  f = np.random.rand(n)
  x = np.zeros(n)

  start_time = time.time()# Numpy
  X = np.linalg.solve(A, f)
  np_time[iterator - 1] = time.time() - start_time

  start_time = time.time()# My

  for k in range(n):
    f[k] = f[k] / A[k][k]
    A[k] = A[k] / A[k][k]
    for i in range(k + 1, n):
      f[i] = f[i] - f[k] * A[i][k]
      A[i] = A[i] - A[k] * A[i][k]
      A[i][k] = 0

  for i in range(n - 1, -1, -1):
    x[i] = f[i]
    for j in range(i + 1, n):
      x[i] = x[i] - A[i][j] * x[j]

  my_time[iterator - 1] = time.time() - start_time

  print('n = ', n)
  print('My time:', my_time[iterator - 1])
  print('Np time:', np_time[iterator - 1])
  print()

plot = np.linspace(100, size * 100, size)
plt.title('Gauss')
plt.plot(plot, np_time, label = 'Numpy time')
plt.plot(plot, my_time, label = 'My time')
plt.legend()
plt.ylabel('Time')
plt.xlabel('Matrix size')
plt.show()