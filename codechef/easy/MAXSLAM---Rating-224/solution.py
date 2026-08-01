# cook your dish here
import math
x=int(input())
if x>=25:
    print(0)
else:
    k=25-x
    print(math.ceil(k/4))