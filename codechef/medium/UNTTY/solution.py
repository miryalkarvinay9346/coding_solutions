# cook your dish here
s=input()
a=list(s)
i=0
k=[]
for i in range(len(s)):
    if s[i]=="#":
        if len(k)==0 or not k:
            continue
        else:
            k.pop()
    else:
        k.append(s[i])
print("".join(k))
        
        