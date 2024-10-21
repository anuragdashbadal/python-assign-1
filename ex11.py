# Exercise - 11 Write a Python program that:
# 1. Takes input of 3 students' names and their respective scores in 3 subjects.
# 2. Stores them in a nested list.
# 3. Prints each student's name and their average score.

def calculate_average(scores):
    return sum(scores) / len(scores)

students = []

for i in range(3):
    name = input(f"Enter The Name Of Student {i + 1}:")
    scores = []
    for j in range(3):
        score = float(input(f"Enter the Score of Student {j + 1}: "))
        scores.append(score)
    students.append([name,scores])
    
        
