# cook your dish here
n,k=map(int,input().split())
t=list(map(int,input().split()))
a=t[k]
c=0
for i  in range(n):
    if i<=k:
        if t[i]<a:
            c=c+t[i]
        else:
            c=c+a
    else:
        if t[i]<a:
            c=c+t[i]
        else:
            c=c+a
print(c)