# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    if min(a)>m:
        print(0)
        continue
    c=0
    l=0
    s=0
    for i in range(n):
        s+=a[i]
        while s>m:
            s=s-a[l]
            l+=1
        c=max(c,i-l+1)
    print(c)
        