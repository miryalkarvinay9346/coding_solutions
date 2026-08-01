# cook your dish here
import math
n=int(input())
if n%3==0:
    print(n)
else:
    print(n+1 if (n+1)%3==0 else n-1)