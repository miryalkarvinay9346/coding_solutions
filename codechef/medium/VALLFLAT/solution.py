# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    m=2000
    for i in range(n-1):
        for j in range(n):
            if a[i]!=a[j] and i!=j:
                if a[i]<min(a[i-1],a[i+1]):
                    a[i-1]=a[i]
                    a[i+1]=a[i]
                    m=min(m,sum(a))
    print(m)