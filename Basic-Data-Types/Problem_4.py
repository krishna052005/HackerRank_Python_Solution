-- Problem: Finding the percentage
--Platform: HackerRank
--Difficulty: Easy

Question: The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

n = int(input())
student_marks = {}

for _ in range(n):
    name, *marks = input().split()
    student_marks[name] = list(map(float, marks))

query_name = input()

average = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{average:.2f}")
