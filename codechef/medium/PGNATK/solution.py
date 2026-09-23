# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    c=0
    for i in range(1,max(n,k*n)):
        if i==i*k:
            c+=1
        else:
            c+=1
            n=n-1
        if n==0 :
            print(c)
            break
        
        