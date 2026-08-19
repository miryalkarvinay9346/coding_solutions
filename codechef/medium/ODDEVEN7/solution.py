# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    oc=0
    ec=0
    for i in a:
        if i%2==0:
            ec+=1
        else:
            oc+=1
    if abs(ec-oc)<=1:
        print(oc+ec)
    else:
        print(2*(min(oc,ec))+1)