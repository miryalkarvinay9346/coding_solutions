# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    m=max(a)
    c=0
    for i in range(n):
        k=max(m,2*a[i])
        b=s+a[i]-k
        c=max(c,b)
    print(c)
        