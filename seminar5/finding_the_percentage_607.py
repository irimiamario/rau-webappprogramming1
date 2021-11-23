n = input("Please enter the number of students: ")
n = int(n)

catalogue = {}
for i in range(n):
    line = input()
    line_elements = line.split(" ")
    name = line_elements[0]
    marks_int = []
    for mark in line_elements[1:]:
        mark_int = float(mark)
        marks_int.append(mark_int)
    catalogue[name] = marks_int

student_name = input("Please enter a student name: ")
if student_name in catalogue.keys():
    average = 0
    for mark in catalogue[student_name]:
        average += mark
    average = average / len(catalogue[student_name])
    average = round(average, 2)

    print(f"Student {student_name} has an {average} average.")