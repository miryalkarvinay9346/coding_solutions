# cook your dish here
for _ in range(int(input())):
    l,b,w=map(int,input().split())
    a=2*(l*b+b*w+w*l)
    print(1000//a)
    