# cook your dish here
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
k=[]
for i in range(m):
    o=b.count(b[i])
    g=a.count(b[i])
    if o==g:
        continue
    else:
        d=o-g
        k.append(b[i])
#k.sort()
print(k)