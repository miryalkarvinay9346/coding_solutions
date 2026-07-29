# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    c=0
    """
    if y>=z:
        if z>=x+y:
            print(1)
        else:
            print(-1)
        continue
        """
    for i in range(1,101):
        x=x+y
        c=c+z
        if x<=c:
            print(i)
            break
        else:
            print(-1)