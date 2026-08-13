# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c1=0
    c2=0
    for i in range(0,n,2):
        c1+=a[i]
    for j in range(1,n,2):
        c2+=a[j]
    print(max(c1,c2))