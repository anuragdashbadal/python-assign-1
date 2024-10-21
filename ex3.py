# Exercise - 3  Write a Python program that:
# 1. Takes three boolean values (True or False) as input.
# 2. Uses and, or, and not operators to return the result of combining them.

def logical_operations(val1,val2,val3):
    #using and operator
    and_result = val1 and val2 and val3
    #using or operator
    or_result = val1 or val2 or val3
    #Using not operator on each value
    not_val1 = not val1
    not_val2 = not val2
    not_val3 = not val3
    
#Display Results
    print(f"Result Of AND Operations: {and_result}")
    print(f"Result Of OR Operation: {or_result}")
    print(f"Not {val1}: {not_val1}")
    print(f"Not {val2}: {not_val2}")
    print(f"Not {val3}: {not_val3}")
    
    
#Input from User(Converting String Input to Boolean)
    val1  = input("Enter First Boolean Value (True/False): ").strip().capitalize() == "True"
    val2  = input("Enter First Boolean Value (True/False): ").strip().capitalize() == "True"
    val3  = input("Enter First Boolean Value (True/False): ").strip().capitalize() == "True"
    
    logical_operations(val1,val2,val3)