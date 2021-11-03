n = input("Number of students: ")
n = int(n)

catalogue = {}
for i in range(n):
    line = input()
    line_elements = line.split(" ")
    name = line_elements[0]
    marks = line_elements[1:]
    marks_int = []
    for mark in marks:
        mark_int = float(mark)
        marks_int.append(mark_int)
    catalogue[name] = marks_int

student = input()
if student in catalogue.keys():
    average_mark = 0
    for mark in catalogue[student]:
        average_mark = average_mark + mark
    average_mark = average_mark / len(catalogue[student])

    print(f"Student {student} has an average {average_mark}.")


