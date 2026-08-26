# cook your dish here
for _ in range(int(input())):
    a,b,p,q,r=map(int,input().split())
    if a==b:
        print(r*a)
    else:
        c=p*a+(q*b)
        print(c)