# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    p=a[0]
    c=0
    for i in a:
        if i>=p:
            c+=1
    print(c)