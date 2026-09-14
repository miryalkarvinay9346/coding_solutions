# cook your dish here
n=int(input())
a=list(map(int,input().split()))
m=(a[0]+a[-1])//2
if m==a[n//2]:
    print(m)
else:
    k=min(a[n//2+1],a[(n//2)-1])
    print(k)