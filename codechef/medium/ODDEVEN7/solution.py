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
        if oc%2!=0:
            print(oc+2)
        elif ev%2==0:
            print(ec+2)