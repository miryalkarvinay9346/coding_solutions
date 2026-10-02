# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    a=max((x-y),(x-z))
    b=min((x+y),(x+z))
    print(abs(a-b))
        
    