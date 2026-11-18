# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    if  x%2==0:
        count=n//2
    else:
        count=(n+1)//2
    if (x+x)%2==0:
        count-=1
    print(count)