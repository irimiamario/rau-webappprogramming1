def average(marks):
    avg = 0
    for mark in marks:
        avg = avg + mark
    avg = avg / len(marks)
    return round(avg, 2)


n = input("Please enter the number of students: ")
n = int(n)

lines = []
for i in range(n):
    line = input()
    lines.append(line)

# catalogue = {
#     "andrei": [10, 20, 30]
# }
catalogue = {}
for line in lines:
    line_elements = line.split(" ")
    student_name = line_elements[0]
    n_marks = len(line_elements[1:])
    student_marks = []
    for i in range(1, n_marks + 1):
        student_mark = float(line_elements[i])
        student_marks.append(student_mark)
    catalogue[student_name] = student_marks

current_student = input("Please enter student's name: ")
students = list(catalogue.keys())

if current_student in students:
    avg = average(catalogue[current_student])
    print(f"Student {current_student} has an average of {avg}.")
else:
    print(f"Student {current_student} not found. Please try again using one of the following students: {students}.")


