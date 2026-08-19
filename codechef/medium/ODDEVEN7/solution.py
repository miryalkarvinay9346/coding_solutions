# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    oc=0
    ec=0
    for i in a:
        if i%2==0:
            ec=0
        else:
            ec=0
    if oc==ec:
        print(n)
    else:
        