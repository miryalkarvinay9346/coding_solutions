# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    print("YES" if a.count("a")+b.count("a")==len(a) or a.count("b")+b.count("b")==len(b) else "NO")