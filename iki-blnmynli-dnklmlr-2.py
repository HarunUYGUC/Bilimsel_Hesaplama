""" Lineer İnterpolasyon Yöntemi """

def f(x):
    return (x**2 - 3*x - 4)

x1 = 0
x2 = 10

if (f(x1) * f(x2) == 0):
    print("En az bir tahmin deklemin kökü.")
elif (f(x1) * f(x2) > 0):
    print("Aralıkta kök yok.")
else:
    # xorta = (x1 + x2) / 2
    xorta = x2 - (f(x2) * (x1 - x2)) / (f(x1) - f(x2)) # Lineer İnterpolasyon Yöntemi

    while (f(xorta) != 0):
        if (f(x1) * f(xorta) > 0):
            x1 = xorta
        else:
            x2 = xorta

        xorta = (x1 + x2) / 2

        print(xorta)
