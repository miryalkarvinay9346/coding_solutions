# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    p=0
    a=s.count("1")
    print(max(1,a-k))