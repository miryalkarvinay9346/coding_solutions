# cook your dish here
n,k=map(int,input().split())
a=list(map(int,input().split()))
v=[]
p=n-k+1
for i in range(p):
    b=a[i:i+k]
    b.sort()
    if len(b)%2==0:
        s=b[(len(b)//2)-1]
        v.append(s)
    else:
        v.append(b[(len(b))//2])
print(v)