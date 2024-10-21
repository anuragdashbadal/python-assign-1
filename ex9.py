#Exercise - 9   Write a Python program that:
# 1. Asks the user to input a list of 5 numbers.
# 2. Sorts the list in ascending order and displays it.
# 3. Sorts the list in descending order and displays it.


def sort_numbers(numbers):
    ascending_order = sorted(numbers)
    print("List Sorted In Ascending Order: ",ascending_order)
    
    descending_order = sorted(numbers, reverse=True)
    print("List Sorted In Descending Order: ",descending_order)
    
numbers = []
for i in range(5):
    number = float(input(f"Enter NUmber {i+1}: "))
    numbers.append(number)
    
sort_numbers(numbers)        