# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=0
    while True:
        if n%3==0:
            print(c)
            break
        else:
            c+=1
            n=round(n/2)*5