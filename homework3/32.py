import numpy as np
import matplotlib.pyplot as plt

def lagrange(x, y, t):
	n = len(x)
	m = len(y)
	s = 0
	for j in range(m):
		phi = 1
		for i in range(n):
			if i != j:
				phi = phi * (t - x[i]) / (x[j] - x[i])
		s = s + y[j] * phi
	return s

train_x = open('data2/train.dat', 'r')
train_y = open('data2/train.ans', 'r')
test_x = open('data2/test.dat', 'r')
test_y = open('data2/test.ans', 'w')

x = [float(i) for i in train_x.readline().split()]
y = [float(i) for i in train_y.readline().split()]
z = [float(i) for i in  test_x.readline().split()]
n = len(x)
m = len(z)

f = np.zeros(m)

for i in range(m):
	f[i] = lagrange(x, y, z[i])
	test_y.write(str(f[i]) + ' ')

print('Count train = ', n)
print('x = ', x)
print('y = ', y)
print('Count of test = ', m)
print('z = ', z)
print('f = ', f)

min_xz = min(np.min(x), np.min(z))
max_xz = max(np.max(x), np.max(z))

x_plt = np.linspace(min_xz , max_xz, 50)
y_plt = np.zeros(len(x_plt))
for j in range(len(x_plt)):
	y_plt[j] = lagrange(x, y, x_plt[j])

train_x.close()
train_y.close()
test_x.close()
test_y.close()

plt.plot(x_plt, y_plt, 'b', label = 'lagrange')
plt.plot(x, y, 'o', label = 'train') 
plt.plot(z, f, 'r*', label = 'test')
plt.ylabel('y(x), f(z)')
plt.xlabel('x, z')
plt.legend()
plt.grid()
plt.show()