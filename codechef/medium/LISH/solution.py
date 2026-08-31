# cook your dish here
w=int(input())
n=int(input())
a=list(map(int,input().split()))
if 2*sum(a)<w:3
    print(-1)
else:
    a.sort(reverse=True)
    c=0
    m=w
    for i in range(n):
        for j in range(n):
            if m<=0:
                break
            m=m-a[i]
            c+=1
        if m<=0:
            break
    print(c)
    