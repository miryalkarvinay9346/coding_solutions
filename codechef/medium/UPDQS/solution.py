# cook your dish here
for _ in range(int(input())):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    i=[]
    x=[]
    for m in range(q):
        v,y=map(int,input().split())
        i.append(v)
        x.append(y)
    for k in range(n-1):
        s=a[i+1]+a[i-1]+a[i]
        a[i]=min(s,a[i])
    print(sum(a))