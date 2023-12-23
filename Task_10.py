i=1;
while i<1000:
    g = 1
    k=0
    while g<i:
        if i%g==0:
            k=k+1
        g = g + 1
    if k==5:
        print(i)
        g=g+1
    i+=1