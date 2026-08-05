# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=0
    for i in range(n):
        for j in range(i,n):
            b=a[j]-j+i
    print(b)