# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=list(map(int,input().split()))
    a=0
    for i in range(n):
        
        for j in range(n):
            if c[i]<=c[j] and c[j] >=c[i]:
                k=c[i]+c[j]
                a=max(k,max(c))
    print(a)
                
                