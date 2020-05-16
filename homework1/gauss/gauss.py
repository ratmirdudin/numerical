import numpy as np
import time
import matplotlib.pyplot as plt

print('n = ', end='')
n = int(input())
A = np.random.rand(n, n)
f = np.random.rand(n)
x = [0] * n

start_time = time.time()
X = np.linalg.solve(A, f)
numpy_time = time.time() - start_time
print('numpy time:', numpy_time)

start_time = time.time()
for k in range(n):
  f[k] = f[k] / A[k][k]
  A[k] = A[k] / A[k][k]
  for i in range(k + 1, n):
    f[i] = f[i] - A[i][k] * f[k]
    A[i] = A[i] - A[i][k] * A[k]
    A[i][k] = 0

for i in range(n - 1, -1, -1):
  x[i] = f[i]
  for j in range(i + 1, n):
    x[i] = x[i] - A[i][j] * x[j]

my_time = time.time() - start_time
print('my time: ', my_time)

print('\n||x - X|| = ', max(np.absolute(x - X)))

plt.grid()
plt.title('My time = ' + str(my_time))
plt.plot(x, 'b-', label='My solve')
#plt.plot(X, 'r*-', label='Numpy solve')
plt.show()