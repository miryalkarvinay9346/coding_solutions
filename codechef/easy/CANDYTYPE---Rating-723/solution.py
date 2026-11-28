# cook your dish here
from collections import Counter
T=int(input())
for i in range(T):
    N=int(input())
    colors=list(map(int,input().split()))
    freq=Counter(colors)
    maximum=max(freq.values())
    candidates=[num for num,count in freq.items() if count==maximum ]
    print(min(candidates))