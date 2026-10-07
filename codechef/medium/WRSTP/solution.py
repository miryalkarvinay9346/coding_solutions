# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    # U D L R
    if s.count("U")==s.count("D") and s.count("L")==s.count("R"):
        print("NO")
    