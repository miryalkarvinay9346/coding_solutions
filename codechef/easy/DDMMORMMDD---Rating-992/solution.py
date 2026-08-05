t = int(input())
while t > 0:
    s = input()
    # Your code goes here
    x=int(s[:2])
    y=int(s[3:5])
    if (x>=1 and x<=12) and (y>=1 and y<=12):
        print("BOTH")
    else:
        if x>=1 and x<=12:
            print("MM/DD/YYYY")
        else:
            print("DD/MM/YYYY")
    t -= 1
