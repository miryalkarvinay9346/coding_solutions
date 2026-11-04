# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        oc=0
        for j in range(i,n):
            if a[j]%2!=0:
                oc+=1
            if oc%2==0:
                l=j-i+1
                c=max(c,l)
    print(c)
                