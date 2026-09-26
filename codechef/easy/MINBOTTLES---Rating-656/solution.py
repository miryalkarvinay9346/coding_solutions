# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    print((s+x-1)//x)
    