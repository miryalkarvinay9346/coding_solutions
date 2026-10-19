# cook your dish here
for _ in range(int(input())):
    X,Y=map(int,input().split())
    if (5*X)<=((2*Y)+X):
        print(5*X)
    else:
        print((2*Y)+X)