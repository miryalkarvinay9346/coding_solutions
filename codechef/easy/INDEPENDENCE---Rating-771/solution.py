# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().strip().split())
    max_value=max(a,b,c)
    other=a+b+c-max_value
    if max_value <= (other+1):
        print("Yes")
    else:
        print("No")