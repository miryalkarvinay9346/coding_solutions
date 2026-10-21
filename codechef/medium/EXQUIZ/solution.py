# cook your dish here
for _ in range(int(input())):
    n,s=map(int,input().split())
    if s<=0:
        if -s<=n:
            if s==0:
                print(0)
            else:
                print(-s)
        else:
            print(0)
        continue
    k=(s+3)//4
    c=(n+s)//5
    if k>c:
        print(-1)
    else:
        print(5*k-s)