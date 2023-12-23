x = float(input("Enter a number: "))
i = 1
k = 0

while True:
    k = (1/i * ((x-1)/(x+1))**i) + k
    i += 2
    if i > 100:
        break

print(k)
