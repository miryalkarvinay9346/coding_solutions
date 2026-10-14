# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    print(min(a[-2]-min(a),max(a)-a[1]))
    """
    min(second_max(a)-min(a),max(a)-second_min(a))
    """
    