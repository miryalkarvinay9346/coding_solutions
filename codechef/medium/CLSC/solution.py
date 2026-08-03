# cook your dish here
n=int(input())
a=list(map(int,input().split()))
a.sort()
m=float('inf')
for i in range(n-1):
    if abs(a[i]-a[i+1])<m:
        m=abs(a[i]-a[i+1])
print(m)