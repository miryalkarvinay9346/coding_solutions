# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    # U D L R
    x=0
    y=0
    if s.count("U")==s.count("D") and s.count("L")==s.count("R"):
        print("NO")
    else:
        print("HI")