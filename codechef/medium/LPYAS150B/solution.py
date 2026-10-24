def check_palindrome(s):
    # Complete the function
    if s==s[::-1]:
        return "YES"
    else:
        return "NO"
def main():
    test_cases = int(input())
    # Complete the function
    for _ in range(test_cases):
        s=input()
        k=check_palindrome(s)
        print(k)

main()