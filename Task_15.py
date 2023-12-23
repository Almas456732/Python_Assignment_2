x=int(input("Enter"))
i=3
k=1
j=0
c=1
while True:
    if c%2!=0:
        j = x ** i / (i * k) + j
    if c%2==0:
        j = -1*(x ** i / (i * k)) + j
    k = k * i
    i+=2
    c+=1
    if c > 100:
        break
print(j)