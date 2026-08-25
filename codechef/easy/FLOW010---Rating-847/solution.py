# cook your dish here
for _ in range(int(input())):
    a=input().lower()
    if a=="b":
        print("BattleShip")
    elif a=="c":
        print("Cruiser")
    elif a=="d":
        print("Destroyer")
    else:
        print("Frigate")