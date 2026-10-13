# cook your dish here
for _ in range(int(input())):
    m,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=x*y
    c=[0]*101
    for k in a:
        i=max(1,k-b)
        j=min(100,k+b)
        for p in range(i,j+1):
            c[p]=1
    print(100-sum(c))
            