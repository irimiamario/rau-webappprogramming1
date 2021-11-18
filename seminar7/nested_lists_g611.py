def sorting_function(x):
    return x[1]


# get number of students
n = int(input("Number of students: "))

# get grades
grades = []
for i in range(n):
    student_name = input()
    student_grade = float(input())
    grades.append([student_name, student_grade])

# sort [student, grade] by grade
# sorted_grades = sorted(grades, key=sorting_function)

# get second lowest mark
student_grades = []
for entry in grades:
    student_grades.append(entry[1])
student_grades = set(student_grades)
student_grades = list(student_grades)
student_grades = sorted(student_grades)
second_lowest_mark = student_grades[1]

# get students with second lowest mark
students = []
for entry in grades:
    if entry[1] == second_lowest_mark:
        students.append(entry[0])

# sort students by name
students = sorted(students)

# print result
print(students)
