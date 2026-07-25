# cook your dish here
for  _ in range(int(input())):
    d=map(int,input().split())
    n=input()
    print("yes" if ('0' in n) or('5' in n) else "no" )
    