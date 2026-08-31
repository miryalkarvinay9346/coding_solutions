# cook your dish here
w=int(input())
n=int(input())
a=list(map(int,input().split()))
if 2*sum(a)<20:
    print(-1)
else:
    a.sort(reverse=True)
    c=0
    m=w
    for i in range(n):
        k=w%a[i]
        if k>0 :
            c+=(w//a[i])
            m=m-(w//a[i])*a[i]
    print(c)
    #print(25//10)