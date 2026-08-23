# cook your dish here
for _ in range(int(input())):
    n=int(input())
    ed,od=0,0
    for i in range(1,n+1):
        if n%i==0:
            if i%2==0:
                ed+=1
            else:
                od+=1
    if ed==od:
        print(0)
    elif ed>od:
        print(1)
    else:
        print(-1)