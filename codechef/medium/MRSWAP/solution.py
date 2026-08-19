# cook your dish here
for  _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    x,y=0,2*n-1
    while x<y:
        s+=max(a[x],a[y])
        x=x+1
        y=y-1
    print(s)