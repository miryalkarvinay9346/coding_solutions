# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=list(map(int,input().split()))
    a=max(c)
    for i in range(n):
        for j in range(i+1,n):
            if c[i]<=c[j] and c[j] >=c[i]:
                k=c[i]+c[j]
                a=max(k,a)
    print(a)
                
                