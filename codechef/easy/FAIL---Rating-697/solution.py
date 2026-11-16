# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    print("Yes" if sum(a)//n >=40 else "No")