# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    x=a[0]
    for i in range(1,n):
        if a[i]<=x:
            a[i]=a[i]+1
        else:
            a[i]=a[i]-1
        if a==a[::-1]:
            c=1
            break
        #x=a[]
    if c:
        print("YES")
    else:
        print("NO")