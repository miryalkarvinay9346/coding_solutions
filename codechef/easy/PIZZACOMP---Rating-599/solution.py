for _ in range(int(input())):
    A, B = map(int, input().split())
    # Compare 100/A and 225/B using cross-multiplication
    small_value = 100 * B
    large_value = 225 * A
    
    if small_value > large_value:
        print("Small")
    elif small_value < large_value:
        print("Large")
    else:
        print("Equal")