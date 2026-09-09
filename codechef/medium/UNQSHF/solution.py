# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    print("YES" if a.count("a")+b.count("b")==len(a) else "NO")