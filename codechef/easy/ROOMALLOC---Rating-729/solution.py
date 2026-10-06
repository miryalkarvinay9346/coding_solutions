# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        if a[i]<=2:
            c+=1
        else:
            c+=a[i]//2
            c+=a[i]%2
    print(c)