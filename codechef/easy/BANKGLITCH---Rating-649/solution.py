# cook your dish here
for _ in range(int(input())):
    a,b,x,y=map(int,input().split())
    """
    while a>=x:
        a-=x
        b+=y
    print(a+b)
    """
    trades = a // x# Calculate the maximum number of possible trades
    # Each trade increases the total money by (y - x)
    answer = a+ b + trades * (y-x)
    print(answer)
    