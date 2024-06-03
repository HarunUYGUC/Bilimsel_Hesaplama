from math import pi

t = 0
hedef = 1
s = 8
v = 12
adim = 1000000
h = (hedef - t) / adim

for i in range(adim):
    sg = s + v*h
    v -= pi**2 / 36 * s * h
    s = sg

print(s, v)
