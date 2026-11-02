# cook your dish here
n,m=map(int,input().split())
a=[]
for i in range(n):
    k=list(map(int,input().split()))
    a.append(k)
print(a)
"""
d=[]
for i in range(n):
    for j in range(m):
        if i==j:
            d.append(a[i][j])
d.sort()
k=0
for i in range(n):
    for j in range(m):
        if i==j:
            a[i]=d[k]
            k+=1
print(a)
print(d)
"""