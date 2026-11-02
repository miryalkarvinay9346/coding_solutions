# cook your dish here
for _ in range(int(input())):
    x,a,b=map(int,input().split())
    if x<80:
        k=(80-x)*a+20*b
        print(k)
    else:
        print((100-x)*b)
        