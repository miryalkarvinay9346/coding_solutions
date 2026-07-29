# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    c=0
    if y>=z:
        if z>=x+y:
            print(1)
        else:
            print(-1)
    else:
        m=0
        for i in range(1,101):
            m+=1
            x=x+y
            if z*m>=x:
                print(m)
                break
            