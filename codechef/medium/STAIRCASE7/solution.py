# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    b={}
    for i in range(n):
        k=a[i]-i
        if a[i]-i in b:
            b[k]+=1
        else:
            b[k]=1
        c=max(c,b[k])
    print(n-c)