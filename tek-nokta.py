from math import e

x = 0

for i in range(200):
    x = e**(-2*x)
    print(x)
