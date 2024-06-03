y, z = -42, 42000

for i in range(100):
    x = (13 - 3*y - z) / 9
    y = (6 + z - 2*x) / 5
    z = (2 + 6*x) / 8
    
    print(x, y, z)
