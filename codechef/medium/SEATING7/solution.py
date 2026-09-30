# cook your dish here
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    for i in range(1,n+1):
        if k==0:
            break
        if i not in a :
            b.append(i)
            k-=1
    print(*b)
            