# cook your dish here
a,b,c,d=map(int,input().split())
s=0
if a==0 or b==0 or c==0 or d==0:
    print("YES")
elif a+b==0 or b+c==0 or c+d==0 or d+a==0 or a+c==0 or a+d==0 or b+d==0:
    print("YES")
elif a+b+c==0 or a+b+d==0 or b+c+d==0 or c+d+a==0:
    print("YES")
elif a+b+c+d==0:
    print("YES")
else:
    print("NO")
    