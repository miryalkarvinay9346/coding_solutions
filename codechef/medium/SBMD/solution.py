# cook your dish here
n,k=map(int,input().split())
a=list(map(int,input().split()))
v=[]
for i in range(len(a)):
    b=a[i:i+k]
    b.sort(revese=True)
    if len(b)%2==0:
        s=b[]