# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        k=0
        for j in range(n):
            if a[i]-i==a[j]:
                k+=1
        c=max(c,k)
    print(n-c)