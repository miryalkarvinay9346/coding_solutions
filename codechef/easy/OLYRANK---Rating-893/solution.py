# cook your dish here
for _ in range(int(input())):
    g1,s1,b1,g2,s2,b2=map(int,input().split())
    print(1 if g1+s1+b1>g2+s2+b2 else 2)