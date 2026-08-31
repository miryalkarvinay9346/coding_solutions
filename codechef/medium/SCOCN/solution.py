# cook your dish here
n=int(input())
a=list(map(int,input().split()))
x=int(input())
if x not in a:
    print(-1)
elif a.count(x)==1:
    print(-2)
else:
    k=0
    m=0
    for i in range(n):
        for j in range(n):
            if a[j]==x:
                k+=1
            if k==2:
                print(j)
                m=1
                break
        if m:
            break
            
            
            