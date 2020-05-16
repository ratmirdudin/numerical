import numpy as np
import scipy.linalg as sl
import time
import matplotlib.pyplot as plt
import random

def tridiagonal_matrix(n):
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
	a = [0] * n
	b = [0] * n
	c = [0] * n
	for i in range(n):
		for j in range(i - 1, i + 2):
			if j == i - 1 and j != -1:
				a[i - 1] = A[i][j]
			if j == i:
				c[i] = A[i][j]
			if j == i + 1 and j != n:
				b[i + 1] = A[i][j]	
	return np.array([b, c, a])

print('n = ', end='')
n = int(input())
A = tridiagonal_matrix(n)
f = np.random.rand(n)
x = [0] * n
abc = create_abc(A, n)

start_time = time.time()
X = sl.solve_banded((1, 1), abc, f)
numpy_time = time.time() - start_time
print('numpy time:', numpy_time, '\n')

start_time = time.time()
m = 1;
#a - sub-diagonal elems
#b - supra-diagonal elems
#c - diagonal elems
for i in range(1, n):
	m = A[i][i - 1] / A[i - 1][i - 1]
	A[i][i] = A[i][i] - m * A[i - 1][i]
	f[i] = f[i] - m * f[i - 1]

x[n - 1] = f[n - 1] / A[n - 1][n - 1];
for i in range(n - 2, -1, -1):
  x[i] = (f[i] - A[i][i + 1] * x[i + 1]) / A[i][i]

my_time = time.time() - start_time
print('my time: ', my_time)

print('\n||x - X|| = ', max(np.absolute(x - X)))

plt.grid()
plt.title('My time = ' + str(my_time))
plt.plot(x, 'b-', label='My solve')
#plt.plot(X, 'r*-', label='Numpy solve')
plt.show()