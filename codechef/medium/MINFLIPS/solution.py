# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if sum(a)==0:
        print(0)
    else:
        if n%2!=0:
            print(-1)
        else:
            k=a.count(1)-(n//2)
            print(k)