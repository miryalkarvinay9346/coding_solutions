# cook your dish here
for _ in range(int(input())):
    x=int(input())
    k=x%3
    print(k%3 if k%3==0 else 3-k%3)