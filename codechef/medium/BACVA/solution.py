# cook your dish here
for _ in range(int(input())):
    a=int(input())
    s=0
    while a>0:
        s+=a%10
        a=a//10
    print("Valid" if s==10 else "Invalid")