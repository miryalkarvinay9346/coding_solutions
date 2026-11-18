# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    if x%2==0:
        print((n//2)-1)
    else:
        print(n//2)