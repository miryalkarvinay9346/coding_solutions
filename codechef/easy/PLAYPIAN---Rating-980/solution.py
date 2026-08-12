# cook your dish here
for _ in range(int(input())):
    s=input()
    c=0
    for i in range(0,len(s)-1,2):
        if  (s[i]=="A" and s[i+1]=="B" ) or (s[i]=="B" and s[i+1]=="A"):
            continue
        else:
            c=1
            break
    print("Yes" if c==0 else "NO")
        