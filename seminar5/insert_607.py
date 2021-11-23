l = []

n = input()
n = int(n)

commands = []
for i in range(n):
    line = input()
    commands.append(line)

for line in commands:
    line_elements = line.split(" ")
    if line_elements[0] == "insert":
        l.insert(int(line_elements[1]), int(line_elements[2]))
    elif line_elements[0] == "print":
        print(l)
    elif line_elements[0] == "remove":
        l.remove(int(line_elements[1]))
    elif line_elements[0] == "append":
        l.append(int(line_elements[1]))
    elif line_elements[0] == "sort":
        l.sort()
    elif line_elements[0] == "pop":
        l.pop()
    elif line_elements[0] == "reverse":
        l.reverse()
