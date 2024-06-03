def f(x):
    return 2.47857 + 2.35929*x + 1.86071*x*x

integral = 0
a, b = 0, 5
n = 50
delta = (b - a) / n

for i in range(n):
    integral += delta * (f(a) + f(a + delta)) / 2
    a += delta

print(integral)
