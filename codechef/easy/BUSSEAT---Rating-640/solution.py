# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    if k<=n:
        print(0)
    else:
        print(2*(k-n))