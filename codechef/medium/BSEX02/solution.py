def main():
    # Write your code here
    for _ in range(int(input())):
        n=int(input())
        c=0
        k=n
        i=1
        while k>0 :
            if k<=i:
                c+=1
                k=k-i
                i+=1
        print(c)
        

if __name__ == "__main__":
    main()
