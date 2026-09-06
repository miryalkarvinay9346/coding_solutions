t = int(input())
while t > 0:
    s = input()
    # Your code goes here
    d=int(s[:2])
    m=int(s[3:5])
    if (d>=1 and d<=12) and (m>=1 and m<=12):
        print("BOTH")
    elif d>=1 and d<=12 :
        print("MM/DD/YYYY")
    else:
        print("DD/MM/YYYY")
    t -= 1
