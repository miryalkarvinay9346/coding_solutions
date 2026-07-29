# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    c=0
    for i in range(1,101):
        x=x+y
        c=c+z
        if x==c:
            print(i)
        if 