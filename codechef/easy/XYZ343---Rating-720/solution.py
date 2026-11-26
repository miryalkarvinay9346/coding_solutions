# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if(x*y<=z):
        print(0)
    else:
       print((x*y-z+y-1)//y)