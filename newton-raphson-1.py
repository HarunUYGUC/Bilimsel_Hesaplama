# Eğri (Parabol)
def f(x):
    return (x**2 - 3*x - 4)

# Eğrinin Türevi (Eğim) => Doğru
def fi(x):
    return (2*x - 3)

# Eğimin x ekseni üzerindeki uzantısı ile eğrinin kökü arasındaki fark.
def hata(x1, x2):
    return (abs((x1 - x2) / x1)) # abs(), absolute (mutlak değer)

x1 = int(input("Tahmin giriniz: "))

"""
for i in range(10):
    x2 = x1 - f(x1) / fi(x1)
    print(x1, x2, hata(x1, x2))
    x1 = x2
"""

x2 = 0

while (hata(x1, x2) > 0):
    x2 = x1 - f(x1) / fi(x1)
    print(x1, x2, hata(x1, x2))
    x1 = x2
    x2 = x1 - f(x1) / fi(x1) # Bunu...
    # ... burada yazmazsak döngü bir kere çalışır ve doğru sonucu vermez.
