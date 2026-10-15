t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))  # Om
    b = list(map(int, input().split()))  # Addy
    t -= 1
    com = 0
    caddy = 0
    co = 0
    ca = 0
    for i in range(n):
        if a[i] > 0:
            co += 1
            com = max(com, co)
        else:
            co = 0
        if b[i] > 0:
            ca += 1
            caddy = max(caddy, ca)
        else:
            ca = 0
    if com == caddy:
        print("Draw")
    elif com > caddy:
        print("Om")
    else:
        print("Addy")