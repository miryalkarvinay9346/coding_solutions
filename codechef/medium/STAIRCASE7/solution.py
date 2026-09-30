# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(2,n+1):
        if a[i]-a[i-1]==1:
            c+=1
    if c==n:
        print