# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    cl=n
    if n==k:
        print("YES")
    else:
        a=0
        i=0
        while i<=n-1:
            if s[i]==s[i+1]:
                cl=cl-1
                i+=2
            if cl==k:
                a=1
                break
            i+=1
        if a==1:
            print("YES")
        else:
            print("NO")
                
                