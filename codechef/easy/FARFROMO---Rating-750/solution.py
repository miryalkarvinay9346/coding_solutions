# cook your dish here
for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    a=(x1**2)+(y1**2)
    b=(x2**2)+(y2**2)
    if a==b:
        print("EQUAL")
    elif a>b:
        print("ALEX")
    else:
        print("BOB")