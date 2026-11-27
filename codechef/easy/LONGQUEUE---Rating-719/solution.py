# cook your dish here
for _ in range(int(input())):
    num_people=int(input())
    wealth=list(map(int,input().split()))
    sushil_wealth=wealth[-1]
    position=num_people
    for i in range(num_people-2,-1,-1):
        if wealth[i]<=sushil_wealth/2:
            position-=1
        else:
            break
    print(position)