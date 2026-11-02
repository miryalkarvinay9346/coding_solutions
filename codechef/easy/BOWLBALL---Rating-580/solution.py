# cook your dish here
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    for i in a:
        if i>=x and i<=y:
            c+=1
    print(c)