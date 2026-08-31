# cook your dish here
w=int(input())
n=int(input())
a=list(map(int,input().split()))
a.sort()
if 2*sum(a)<20:
    print(-1)
else:
    