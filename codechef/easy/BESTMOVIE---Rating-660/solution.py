# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=[]
    b=[]
    for i in range(n):
        k,m=map(int,input().split())
        a.append(k)
        b.append(m)
    c=float('inf')
    v=0
    vc=False
    for i in range(n):
        if a[i]>=7:
            c=min(c,b[i])
        else:
            v=v+1
            if v==n:
                vc=True
                break
    if vc==True:
        print(-1)
    else:
        print(c)
    