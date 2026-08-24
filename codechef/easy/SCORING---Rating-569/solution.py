# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    """
    alice=bob+x
    alice+bob=y
    -----------
    2*bob+x=y
    bob=(y-x)/2
    -------------
    alice=((y-x)/2)+x
    -----------------
    """
    print(((y-x)//2)+x,(y-x)//2)