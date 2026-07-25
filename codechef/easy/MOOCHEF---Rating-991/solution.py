# cook your dish here
for _ in range(int(input())):
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))
    c,hmax,hmin=0,0,0
    for i in range(n):
        if a[i]>=l and a[i]<=r:
            c+=1
        else:
            c-=1
        if c>hmax:
            hmax=c
        if c<hmin:
            hmin=c
    print(hmax,hmin)
    