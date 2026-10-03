# cook your dish here
for _ in range(int(input())):
    n=int(input())
    # How many factors of 5 are present in N!
    c=0
    while n>=5:
        n=n//5
        c+=n
    print(c)