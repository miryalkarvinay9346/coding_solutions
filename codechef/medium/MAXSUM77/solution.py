# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    i=0 
    j=n-1
    c=0
    while(i<=j):
        l=a[i]
        r=a[j]
        if l>r:
            s=s-r
            j=j-1
        else:
            s=s-l
            i=i+1
        c+=1
        if c==k:
            break
    print(s)
        