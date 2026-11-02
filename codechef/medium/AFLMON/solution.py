# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        k=0
    
        for j in range(n):
            if a[i]>=a[j]:
                k=k+1
        
            