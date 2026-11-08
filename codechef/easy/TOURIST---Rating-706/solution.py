# cook your dish here
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    m=float('inf')
    for i in range(n):
        x,y=map(int,input().split())
        ans=abs(x-a)+abs(y-b)
        if ans<m:
            m=ans
    print(m)