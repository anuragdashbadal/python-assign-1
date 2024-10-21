# Exercise - 7 Write a Python program that:
# 1. Creates a list of 5 numbers (input from the user).
# 2. Displays the sum of all the numbers in the list.
# 3. Finds the largest and smallest number in the list

def list_operations(numbers):
    total_sum = sum(numbers)
    print(f"Sum Of All Numbers: {total_sum}")
    
    largest = max(numbers)
    print(f"Largest Number: {largest}")
    
    smallest = min(numbers)
    print(f"Smallest NUmber: {smallest}")
    
    
numbers = []
for i in range(5):
    number = float(input(f"Enter Number {i+1}: "))
    numbers.append(number) # The .append() method in Python is used to add (or append) an item to the end of a list.
    
    
    list_operations(numbers)    
    