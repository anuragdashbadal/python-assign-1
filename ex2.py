# Exercise 2 Write a Python program that asks for two numbers and checks:
# 1. If the first number is greater than the second.
# 2. If the first number is equal to the second.
# 3. If the first number is less than or equal to the second.
# Print the results.


def compare_numbers(num1,num2):
    if num1 > num2:  #Operator
        print(f"{num1}is Greater than {num2}")
    else:
        print(f"{num1}Is Not Greater Than {num2}")
        
        
        if num1 == num2:
            print(f"{num1}is equal to {num2}")
        else:
            print(f"{num1}is not equal to {num2}")
            
            
        if num1 <= num2:
            print(f"{num1} is less than or equal to {num2}")
        else:
            print(f"{num1} is not less than or equal to {num2}")
            
            
num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number:  ")) 

compare_numbers(num1,num2)                       