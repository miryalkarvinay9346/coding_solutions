# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    a,b=min(a,b),max(a,b)
    while a<b:
        a=a*2
    print("YES" if a==b else "NO")