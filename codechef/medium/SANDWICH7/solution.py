# cook your dish here
b,h,c=map(int,input().split())
a=b//2
if h+c<=a:
    print(h+c)
else:
    if h==a:
        print(h)
    elif c==a:
        print(c)
    else:
        