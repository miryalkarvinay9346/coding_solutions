# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=str(bin(n))[2:]
    print("EVEN" if a.count("1")%2==0 else "ODD")