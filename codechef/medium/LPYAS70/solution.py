# cook your dish here
a,b,c=map(int,input().split())
if a<b and b<c:
    print("Increasing")
elif a>b and b>c:
    print("Decreasing")
else:
    print("Neither")