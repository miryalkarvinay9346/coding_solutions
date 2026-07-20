# cook your dish here
n,k=map(int,input().split())
a=list(map(int,input().split()))
v=[]
p=n-k+1
while p>0:
    for i in range(n):
        b=a[i:i+k]
        b.sort(reverse=True)
        if len(b)%2==0:
            s=(b[len(b)//2]+b[(len(b)//2)+1])//2
            v.append(s)

        else:
            v.append(b[(len(b))//2])
    p=p-1    
print(v)