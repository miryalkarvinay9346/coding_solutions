# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=0
    """
    while n%3!=0:
        if n%3==0:
            print(c)
            break
        if (n+1)%3==0:
            c+=1
            print(c)
            break
        else:
            n=((n//2)+1)*5
            #print(n)
            c+=1
            """
    while n%3!=0:
        if (n+1)%3==0:
            c+=1
            n+=1
        else:
            n=((n//2)+1)*5
            c+=1
    print(c)
    