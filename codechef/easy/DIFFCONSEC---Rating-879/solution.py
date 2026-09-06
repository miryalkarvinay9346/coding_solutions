# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    c=0
    #c=s.count("00")+s.count("11")
    for i in range(n-1):
        if s[i]==s[i-1]:
            c+=1
    """
    c=sum(1 for i in range(n - 1) if s[i] == s[i + 1])
    print(c)
    """
    print(c)