# Eğri (Parabol)
def f(x):
    return (x**2 - 3*x - 4)

# Doğru
def fi(x):
    return (2*x - 3)

# Eğimin x ekseni üzerindeki uzantısı ile eğimin kökü arasındaki fark.
def hata(x1, x2):
    return (abs((x1 - x2) / x1)) # abs(), absolute (mutlak değer)

x1 = int(input("Tahmin giriniz: "))
h = 1

while (h > (10**(-3))):
    x2 = x1 - f(x1) / fi(x1)
    h = hata(x1, x2)
    print(x1, h)
    x1 = x2
