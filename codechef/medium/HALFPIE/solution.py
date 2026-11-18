# cook your dish here
for  _ in range((int(input()))):
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    c=max(a)*2
    for i in range(n-1):
        c=min(c,a[i]+a[i+1])
    b=s-c//2
    print(b)
        