xi = [0, 1, 2, 3, 4, 5]
yi = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1]
n = len(xi)

deltaX = xi[1] - xi[0]
altIntegral, ustIntegral, yamuk = 0, 0, 0

for i in range(n - 1):
    altIntegral += deltaX * yi[i]
    ustIntegral += deltaX * yi[i + 1]
    yamuk += deltaX * (yi[i] + yi[i + 1]) / 2

print(altIntegral, ustIntegral, yamuk)
