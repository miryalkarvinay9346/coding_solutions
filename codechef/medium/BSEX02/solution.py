import math
def main():
    # Write your code here
    for _ in range(int(input())):
        n=int(input())
        c=0
        k=int((-1+math.sqrt(1+8*n))//2)
        print(k)
        
if __name__ == "__main__":
    main()
