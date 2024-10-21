
# Exercise - 5  Write a program that asks for the user's name and age, and displays the message in this format:


def display_meassage(name,age):
    print(f"Hello {name}! You are {age} Years Old.")
    
name = input("Enter Your Name: ")
age = input("Enter Your Age: ")

display_meassage(name,age)    