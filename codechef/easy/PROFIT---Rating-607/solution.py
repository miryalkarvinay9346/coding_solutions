# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    p=0
    for i in range(1,n+1):
        if i>x:
            p+=i-x
    print(p)
    