from math import *
x = float(input("Enter a number: "))
i = 1
k = 0

while True:
    if i%2!=0:
        k = -cos(i * x) / (i ** 2) + k
    else :
        k = cos(i * x) / (i ** 2) + k
    i += 1
    print(k)
    if i > 100:
        break

print(k)