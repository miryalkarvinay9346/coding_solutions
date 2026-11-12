# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    s=0
    for i in a:
        if s+i <=k:
            s+=i
            c+=1
        else:
            break
    print(c)