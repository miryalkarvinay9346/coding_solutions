# cook your dish here
for _ in range(int(input())):
    d,n=map(int,input().split())
    s=1
    for i in range(d):
        s=(n*(n+1)//2)
        n=s
    print(s)