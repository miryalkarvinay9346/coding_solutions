# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x+y>z and x+z>y and z+y>x:
        print("0")
    else:
        a=[x,y,z]
        a.sort()
        print(a[2]-(a[1]+a[0])+1)