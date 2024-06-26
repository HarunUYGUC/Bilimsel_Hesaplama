xi = [1, 2, 3, 4, 5, 6, 7]
yi = [0.5, 2.5, 2, 4, 3.5, 6, 5.5]
n = len(xi)

xiyi, xi2, standartSapma, ortalamaHata = 0, 0, 0, 0

for i in range(n):
    xiyi += xi[i] * yi[i]
    xi2 += xi[i]**2
    standartSapma += (yi[i] - sum(yi) / n)**2

a1 = (n * xiyi - sum(xi) * sum(yi)) / (n * xi2 - sum(xi)**2)
a0 = sum(yi) / n - a1 * sum(xi) / n

standartSapma = (standartSapma / (n - 1))**(1/2)

for i in range(n):
    y = a0 + a1 * xi[i]
    ortalamaHata += yi[i] - y

ortalamaHata = (ortalamaHata / (n - 2))**(1/2)

print(a0, a1, standartSapma, ortalamaHata)
