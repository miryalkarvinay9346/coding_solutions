# cook your dish here
n=int(input())
m=1
for i in range(2,11):
    if n%i==0:
        m=i
print(m)