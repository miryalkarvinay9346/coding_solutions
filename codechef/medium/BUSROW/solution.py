# cook your dish here
for  _ in range(int(input())):
    n,m,x=map(int,input().split())
    f=0
    b=n
    c=0
    for i in range(1,n+1):
        if (i-1)*m+1<=x and i*m>=x :
            c=i
    print(min(c,n-c+1))
            