# Excersie 1  : Write a Python program to perform the following operations:
# 1. Add, subtract, multiply, and divide two numbers (input by the user).
# 2. Use the modulus operator to find the remainder of their division.
# 3. Use the exponentiation operator to raise the first number to the power of the second number.
# 4. Perform floor division on the two numbers.


#Function to perform Arithmetic Operations

def arithmetic_operations(num1,num2):
    #addition
    addition = num1 + num2
    #subtraction 
    subtraction = num1 - num2
    #Multiplication 
    multiplication = num1 *  num2
    #Division
    division = num1 / num2 if num2 != 0 else "Undefimed (division by Zero )" # this else is also work in this type of syntax
    #Modulus
    modulus = num1 % num2 if num2 != 0 else "Undefined (Division By Zero)"
    #Exponentitation
    exponentiation = num1 ** num2
    #Floor Division
    floor_division = num1 // num2 if num2 != 0 else "Undefined (Division By Zero)"
    
    return addition, subtraction, multiplication, division, modulus, exponentiation, floor_division


#Input From User
num1 = float(input("Enter The First Number: "))
num2 = float(input("Enter The Second Number: "))

#Performing Operations
results = arithmetic_operations(num1,num2)

#Display Results 
print(f"Addition: {results[0]}")   #The reason for using results[6], results[0], and so on is because the function arithmetic_operations was returning multiple values as a tuple. In Python, when a function returns multiple values, they are stored in a tuple, and each value is accessed by its index. The index starts from 0.
print(f"Subtraction: {results[1]}")
print(f"Multiplication: {results[2]}")
print(f"Division: {results[3]}")
print(f"Modulus: {results[4]}")
print(f"Exponentiation: {results[5]}")
print(f"Floor Division: {results[6]}")