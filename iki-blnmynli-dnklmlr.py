def delta(a, b, c):
    return (b**2 - 4*a*c)

a, b, c = -1, 2, 3

if (delta(a, b, c) < 0):
    print("Denklemin kökü yok.")
elif (delta(a, b, c) == 0):
    kok = -b / 2*a
else:
    kok1 = (-b + delta(a, b, c)**(0.5)) / (2*a)
    kok2 = (-b - delta(a, b, c)**(0.5)) / (2*a)
    print(f"Kökler = {kok1} & {kok2}")
