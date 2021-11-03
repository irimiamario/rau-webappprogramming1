# read data area
n = input("Please enter the number of students: ")
n = int(n)

lines = []
for i in range(n+1):
    info = input()
    lines.append(info)

# process input data area
catalog = {}
for i in range(n):
    student_info = lines[i].split(" ")
    name = student_info[0]
    marks = []
    for mark in student_info[1:len(student_info)]:
        mark = float(mark)
        marks.append(mark)
    catalog[name] = marks

# output area - find average mark
student_marks = catalog[lines[n]]
average_mark = 0
for mark in student_marks:
    average_mark += mark
average_mark = average_mark / len(student_marks)

print(f"Student {lines[n]} has obtained a {average_mark} average.")
