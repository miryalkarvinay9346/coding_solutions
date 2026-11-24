# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=[0]*n
    k[0]=1
    m=a[0]
    for i in range(1,n):
        if a[i]>m:
            k[i]=1
            m=a[i]
    print(" ".join(map(str,k)))
    #print(*k)
    