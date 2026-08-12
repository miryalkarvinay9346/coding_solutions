# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=0
    while True:
        if n%3==0:
            print(c)
            break
        else:
            #c+=1
            if (n+1)%3==0:
                c+=1
                print(c)
                
                break
            else:
                n=round(n/2)*5
                print(n)
            c+=1