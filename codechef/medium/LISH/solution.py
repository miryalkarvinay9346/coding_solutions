# cook your dish here
w=int(input())
n=int(input())
a=list(map(int,input().split()))
if 2*sum(a)<w:
    print(-1)
else:
    a.sort(reverse=True)
    c=0
    m=w
    k=1
    for i in range(n):
        for j in range(n):
            if m<=0:
                k=1
                break
            else:
                m=m-a[i]
                c+=1
        if k:
            break
    print(c)
    