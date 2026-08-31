# cook your dish here
n=int(input())
a=list(map(int,input().split()))
x=int(input())
if x not in a:
    print(-1)
elif a.count(x)==1:
    print(-2)
else:
    for i in range(n):
        if 