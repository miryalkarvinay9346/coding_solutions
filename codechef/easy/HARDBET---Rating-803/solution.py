# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if c<a and c<b:
        print("Alice")
    elif b<c and b<a:
        print("Bob")
    else:
        print("Draw")