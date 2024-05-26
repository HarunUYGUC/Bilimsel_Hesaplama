def f(x):
    return x**3 - 2*x**2 + x

h = 0.01
n = 1

turev = (f(n) - f(n - h)) / h
ikinciturev = (f(n) - 2*f(n - h) + f(n - 2*h)) / h**2

print(turev, ikinciturev)
