# cook your dish here
for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    for i in range(n):
        for j in range(n):
            if abs(p[i]-p[j])>=abs(i-j):
                k=p[i]
                p[i]=p[j]
                p[j]=k