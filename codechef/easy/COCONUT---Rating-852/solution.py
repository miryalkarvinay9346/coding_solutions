# cook your dish here
for _ in range(int(input())):
    xa,xb,ya,yb=map(int,input().split())
    print((ya//xa)+(yb//xb))