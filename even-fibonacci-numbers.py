""" https://projecteuler.net/problem=2 """

a = 1
b = 2
sum = b # sum of the even-valued terms

while (b <= 4000000):
    a, b = b, a
    b = a + b

    if (b % 2 == 0):
        sum += b

print(sum)
