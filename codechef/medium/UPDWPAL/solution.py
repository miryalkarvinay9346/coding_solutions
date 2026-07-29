# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(1,n):
        if a[i]<=x:
            a[i]=a[i]+1
        else:
            a[i]=a[i]-1
        