# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    if sum(a)==0:
        print(c)
    else:
        if n%2==1:
            print(-1)
        else:
            c1=a.count(1)
            c0=n//2
            print(c1-c0)