# cook your dish here
import math
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if  x<=y:
        print(z)
    else:
        k=math.ceil(x/y)
        print(k*z)