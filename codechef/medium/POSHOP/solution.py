# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=list(map(int,input().split()))
    a=0
    for i in range(n):
        s=0
        for j in range(i+1,n):
            if c[i]<=c[j]:
                k=c[i]+c[j]
                a=max(k,a)
    print(a)
                
                