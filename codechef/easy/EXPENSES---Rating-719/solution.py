# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    k=2**x
    while(n):
        k//=2
        n-=1
    print(k)