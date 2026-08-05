# cook your dish here
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    if n<=3:
        print(x*n)
    else:
        print((n-3)*y+x*3)