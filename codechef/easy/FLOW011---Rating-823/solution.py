# cook your dish here
for _ in range(int(input())):
    salary = int(input())
    
    if salary < 1500:
        hra = salary * 0.10
        da = salary * 0.90
    else:
        hra = 500
        da = salary * 0.98
        
    gross_salary = salary + hra + da
    print(f"{gross_salary:.2f}")