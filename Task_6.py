A = int(input())
B = int(input())
i=0;
h=0
while i<10:
    k=B-A
    h=h+k
    B = B + B * 0.03
    i=i+1
print(h)