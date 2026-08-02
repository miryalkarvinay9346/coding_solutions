# cook your dish here
for _ in range(int(input())):
    p,l=map(int,input().split())
    print("YES" if (l/p)*100>=75 else "NO")