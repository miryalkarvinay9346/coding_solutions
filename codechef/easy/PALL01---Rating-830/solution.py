# cook your dish here
for _ in range(int(input())):
    n=input()
    print("wins" if n==n[::-1] else "loses")
    