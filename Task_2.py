number = int(input())

i = 0

while i < number:
    g = 1
    k = 0
    while g < i:
        if i % g == 0:
            k = g + k
        g = g + 1
    if k == i:
        print(k)
    i = i + 1
