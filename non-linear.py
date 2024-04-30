# 1. Denklem
def u(x, y):
    return x**2 + x*y - 10

# 2. Denklem
def v(x, y):
    return y + 3*x*y**2 - 57

# u'nun x'e göre türevi.
def ux(x, y):
    return 2*x + y

# u'nun y'ye göre türevi.
def uy(x, y):
    return x

# v'nin x'e göre türevi.
def vx(x, y):
    return 3*y**2

# v'nin y'ye göre türevi.
def vy(x, y):
    return 1 + 6*x*y

x = float(input("Başlangıç tahmini girin: "))
y = float(input("Başlangıç tahmini girin: "))

# Denklemin kökünün olması için denklem belirli bir değerde 0'a eşit olmalı.
# Denklemdeki değişkenlerin aldığı değere göre denklem 0'a eşit olduğunda yani kökü bulduğumuzda döngüden çıkarız.
while (u(x, y) != 0) and (v(x, y) != 0):
    x -= (u(x, y)*vy(x, y) - v(x, y)*uy(x, y)) / (ux(x, y)*vy(x, y) - uy(x, y)*vx(x, y))
    y += (u(x, y)*vx(x, y) - v(x, y)*ux(x, y)) / (ux(x, y)*vy(x, y) - uy(x, y)*vx(x, y))

print(x, y)
