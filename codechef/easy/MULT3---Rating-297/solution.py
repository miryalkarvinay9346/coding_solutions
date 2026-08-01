# cook your dish here
import math
n=int(input())
if n%3==0:
    print(n)
else:
    print(n+1,math.ceil(n)-1)