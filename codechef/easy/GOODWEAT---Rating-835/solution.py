# cook your dish here
for _ in range(int(input())):
    a,b,c,d,e,f,g=map(int,input().split())
    k=[a,b,c,d,e,f,g]
    print("YES" if k.count(1)>k.count(0) else "NO")