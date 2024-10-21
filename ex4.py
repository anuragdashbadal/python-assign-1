# Exercise 4: String Manipulation
# 1. Take a string input from the user.
# 2. Display the following:
# o The length of the string.
# o The first and last character.
# o The string in reverse order.
# o The string in uppercase and lowercase.


def string_manipulations(s):
    print(f"Length Of The String: {len(s)}")
    
    if len(s) > 0:
        print(f"First Character: {s[0]}")
        print(f"Last Character: {s[-1]}")
        
    print(f"String In Reverse: {s[::-1]}")
        
        
    print(f"String In UpperCase: {s.upper()}")
    print(f"String In LowerCase: {s.lower()}")
        
        
user_string = input("Enter a String: ")
        
string_manipulations(user_string)