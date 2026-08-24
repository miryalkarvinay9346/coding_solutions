# cook your dish here
k=input().lower()
s=''.join(sorted(k))
a=[]
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[i]==s[j] and s[i].isalpha():
            c+=1
    a.append(c)
m=max(a)
ind=a.index(m)
print(s[ind])
