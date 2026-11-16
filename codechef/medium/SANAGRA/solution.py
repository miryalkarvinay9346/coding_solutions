# cook your dish here
a=input()
b=input()
p=[]
for i in a:
    if i.isalnum():
        p.append(i.lower())
q=[]
for j in b:
    if j.isalnum():
        q.append(j.lower())
if sorted(p)==sorted(q):
    print("The sentences are anagrams.")
else:
    print("The sentences are not anagrams.")