t = int(input())
while t > 0:
    s = input()
    # Your code goes here
    c=0
    vowels=['a','e','i','o','u']
    for i in range(len(s)):
        if s[i] in vowels:
            c+=1
            if c>2:
                break
        else:
            c=0
    print("Happy" if c else "Sad")
    
    t -= 1
