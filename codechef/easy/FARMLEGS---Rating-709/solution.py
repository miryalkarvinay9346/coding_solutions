# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n%4==0:
        print(n//4)
    elif n%4!=0:
        print(n//4+((n%4)//2))