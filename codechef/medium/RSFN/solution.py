# cook your dish here
n,q=map(int,input().split())
i=list(map(int,input().split()))
for _ in range(q):
    l,r=map(int,input().split())
    a=[]
    print(sum(i[l-1:r-1]))
