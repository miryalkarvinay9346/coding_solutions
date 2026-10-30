# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    s=(y//2)+min(z,x)
    print(s)