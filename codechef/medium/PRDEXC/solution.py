# cook your dish here
for _ in range(int(input())):
    x,y,p=map(int,input().split())
    c=0
    if x*y>=p:
        print(0)
    else:
        while x*y<p:
            if min(x,y)==x:
                x=x+1
            else:
                y=y+1
            c+=1
        print(c)