# cook your dish here
n=int(input())
a=list(map(int,input().split()))
c=(min(a)+max(a))//2
"""
if m==a[n//2]:
    print(m)
else:
    k=min(a[n//2+1],a[(n//2)-1])
    print(k)
"""
t=a[0]
for i in a:
    d=abs(i-c)
    k=abs(t-c)
    if d<k:
        t=i
    elif d==k:
        if i<t:
            t=i
print(t)