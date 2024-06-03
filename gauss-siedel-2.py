x, z = 10, 1

for i in range(100):
    y = (5 - x + z) / 5
    z = (4*x + 2*y - 4) / 2
    x = 8 - y - 6*z

print(x, y, z)
