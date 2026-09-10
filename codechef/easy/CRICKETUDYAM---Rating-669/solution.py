# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    print('YES' if m<=n-1 else 'NO')