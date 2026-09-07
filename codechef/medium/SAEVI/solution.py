# cook your dish here
n,k=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in range(n):
    if i%2==0 and a[i]>2*k:
        s+=a[i]
print(s)
        