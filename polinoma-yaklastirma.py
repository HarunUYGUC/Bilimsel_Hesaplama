xi = [0, 1, 2, 3, 4, 5]
yi = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1]
n = len(xi)

xi2, xi3, xiyi, xi4, xi2yi, xi5, xi6, xi3yi = 0, 0, 0, 0, 0, 0, 0, 0

for i in range(n):
    xiyi += xi[i] * yi[i]
    xi2yi += xi[i]**2 * yi[i]
    xi3yi += xi[i]**3 * yi[i]
    xi2 += xi[i]**2
    xi3 += xi[i]**3
    xi4 += xi[i]**4
    xi5 += xi[i]**5
    xi6 += xi[i]**6

print(n, sum(xi), xi2, sum(yi), xi3, xi4, xiyi, xi2yi, xi5, xi6, xi3yi)
