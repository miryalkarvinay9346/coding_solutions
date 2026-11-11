# cook your dish here
for _ in range(int(input())):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ca=sum(a)+d
    cb=sum(b)+d
    cab=0+2*d
    for i in range(n):
        cab+=min(a[i],b[i])
    print(min(ca,cb,cab))