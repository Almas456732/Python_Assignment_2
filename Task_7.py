S=int(input())
A = int(input())
B = int(input())
i=0;
h=0
live=S+A-B
while True==True:
    if live<0:
        break
    live = S + A - B
    S=S+(A-B)
    B = B + B * 0.03
    i=i+1
print(i)