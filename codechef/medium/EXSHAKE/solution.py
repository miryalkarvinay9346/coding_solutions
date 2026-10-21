# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    a.sort()
    k=0
    for i in range(n):
        k=k+a[i]
        s=k*(k-1)//2#handshake
        if s<=m:
            c=i+1
        else:
            break
    print(c)