# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    if k>n:
        print("NO")
    else:
        a=(n+1)//2
        if a<=k and k<=n:
            print("YES")
        else:
            print("NO")
        