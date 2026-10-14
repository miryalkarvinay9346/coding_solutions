# cook your dish here
import math
def g(a,b)->int:
    return math.gcd(a,b)
for _ in range(int(input())):
    n=int(input())
    c=0
    for i in range(1,n+1):
        for j in range(i,n+1):
            if g(i,j)==abs(i-j):
                c+=1
    print(c)