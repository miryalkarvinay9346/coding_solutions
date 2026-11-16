# cook your dish here
s=input()
a=[]
for i in s:
    if i.isdigit():
        a.append(i)
if len(a)==0:
    print(-1)
else