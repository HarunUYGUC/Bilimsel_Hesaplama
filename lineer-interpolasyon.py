def f(x):
    return (x**2 - 3*x - 4)

x1 = int(input("İlk tahmini girin: "))
x2 = int(input("İkinci tahmini girin: "))

if (f(x1) * f(x2) > 0):
    print("Bu aralıkta kök yok.")
elif (f(x1) * f(x2) == 0):
    print("Tahminlerinizden en az birisi köktür.")
else:
    for i in range(10):
        xr = x2 - f(x2) * (x1 - x2) / (f(x1) - f(x2))

        if (f(xr) == 0):
            print("Denklemin kökü: ", xr)
            break
        elif (f(x1) * f(xr) < 0):
            x2 = xr
        else:
            x1 = xr

    print(xr)
