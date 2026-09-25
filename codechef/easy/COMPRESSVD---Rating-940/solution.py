# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=n
    for i in range(n-1):
        if a[i]==a[i+1]:
            c-=1
    print(c)
        