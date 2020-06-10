import numpy as np
import matplotlib.pyplot as plt

train_x = open('data1/train.dat', 'r')
train_y = open('data1/train.ans', 'r')
test_x = open('data1/test.dat', 'r')
test_y = open('data1/test.ans', 'w')

x = [float(i) for i in train_x.readline().split()]
y = [float(i) for i in train_y.readline().split()]
z = [float(i) for i in  test_x.readline().split()]
n = len(x)
m = len(z)

A = np.zeros(n)
B = np.zeros(n)
f = np.zeros(m)

for i in range(n - 1):
	A[i] = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
	B[i] = y[i]

for j in range(m):
	for i in range(n - 1):
		if z[j] < x[0]:
			f[j] = A[0] * (z[j] - x[0]) + B[0]
		if z[j] >= x[n - 1]:
			f[j] = A[n - 2] * (z[j] - x[n - 2]) + B[n - 2]
		if x[i] < z[j] <= x[i + 1]:
			f[j] = A[i] * (z[j] - x[i]) + B[i]
	test_y.write(str(f[j]) + ' ')

print('Count train = ', n)
print('x = ', x)
print('y = ', y)
print('Count of test = ', m)
print('z = ', z)
print('f = ', f)

train_x.close()
train_y.close()
test_x.close()
test_y.close()

plt.plot(x, y, 'b', label = 'interpolation')
plt.plot(x, y, 'o', label = 'train') 
plt.plot(z, f, 'r*', label = 'test')
plt.ylabel('y(x), f(z)')
plt.xlabel('x, z')
plt.legend()
plt.grid()
plt.show()