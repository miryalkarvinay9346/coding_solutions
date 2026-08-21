# cook your dish here
for _ in range(int(input())):
    pa,pb,qa,qb=map(int,input().split())
    tp=max(pa,pb)
    tq=max(qa,qb)
    print("P" if tp<tq else ( "Q" if tp>tq else "TIE"))