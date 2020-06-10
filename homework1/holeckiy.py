import numpy as np
import time
import matplotlib.pyplot as plt
from math import *

print('Please, input number, where number * 100 will be sizes of matrix')
size = int(input())
np_time = np.zeros(size)
my_time = np.zeros(size)

for iterator in range(1, size + 1):

  n = iterator * 100

  L = np.tril(np.random.rand(n, n))
  summ = np.sum(np.abs(L), axis = 1)
  diag = summ.max()
  print(diag)
  for i in range(n):
    L[i][i] = diag
  A = L.dot(np.transpose(L))
  f = np.random.rand(n)
  x = np.zeros(n)

  start_time = time.time()# Numpy
  S = np.linalg.cholesky(A)
  np_time[iterator - 1] = time.time() - start_time

  L = np.tril(np.random.rand(n, n))

  start_time = time.time()# My


  for j in range(n):
    for i in range(j, n):
      summ = 0
      if i == j:
        for k in range(j):
          summ = summ + L[j][k] * L[i][k]
        L[i][j] = sqrt(A[j][i] - summ)
        continue
      for k in range(j):
        summ = summ + L[j][k] * L[i][k]
      L[i][j] = (A[j][i] - summ) / L[j][j]

  my_time[iterator - 1] = time.time() - start_time

  A = L.dot(np.transpose(L))
  B = S.dot(np.transpose(S))

  print('n = ', n)
  print('My time:', my_time[iterator - 1])
  print('Np time:', np_time[iterator - 1])
  print()


plot = np.linspace(100, size * 100, size)
plt.title('Cholesky')
plt.plot(plot, np_time, label = 'Numpy time')
plt.plot(plot, my_time, label = 'My time')
plt.legend()
plt.ylabel('Time')
plt.xlabel('Matrix size')
plt.show ()