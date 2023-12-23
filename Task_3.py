k=0
for x in range(100):
    a = int(input())
    if int(a)<0:
        k=a+k
    if a == 0:
        break

print(k)
