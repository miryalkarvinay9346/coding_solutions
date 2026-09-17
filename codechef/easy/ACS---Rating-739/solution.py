# cook your dish here
# cook your dish here
for _ in range(int(input())):
    a=int(input())
    if a//100+a%100<=10:
        print((a//100)+a%10)
    else:
        print(-1)