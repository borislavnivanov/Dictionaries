students_grades = {}
n = int(input())
for _ in range(n):
    student = input()
    grade = float(input())
    if student not in students_grades:
        students_grades[student] = grade
    else:
        students_grades[student] = (students_grades[student] + grade) / 2

for student, grade in students_grades.items():
    if grade >= 4.50:
        print(f'{student} -> {grade:.2f}')
