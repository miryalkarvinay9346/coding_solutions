# cook your dish here
for _ in range(int(input())):
    n,d=map(int,input().split())
    c=n
    s=len(str(n))+1
    while True:
        if str(d) not in str(c):
            print(c)
            break
        else:
            c=c+1