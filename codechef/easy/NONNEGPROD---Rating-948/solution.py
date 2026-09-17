# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if 0 in a:
        print(0)
    else:
        c=0
        for i in a:
            if i<0:
                c+=1
        if c%2!=0:
            print(1)
        else:
            print(0)