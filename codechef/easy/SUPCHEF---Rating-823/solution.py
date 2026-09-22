# cook your dish here
for _ in range(int(input())):
    m,n,k=map(int,input().split())
    print("YES" if n*k<m else "NO")