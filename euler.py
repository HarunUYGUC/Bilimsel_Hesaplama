def f(x, y):
    return -y / x

a = 4
b = 7
y = 0.75
h = 0.0001
n = int((b - a) / h)

for i in range(n):
    y += f(a, y) * h
    a += h
    
print(y, n)
