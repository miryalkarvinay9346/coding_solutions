# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    print("YES" if sorted(a)==sorted(b) else "NO")