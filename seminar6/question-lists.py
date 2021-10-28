l = []
n_commands = input()
n_commands = int(n_commands)

for i in range(0, n_commands):
    command = input("Please enter a command:")
    command_data = command.split(" ")
    if command_data[0] == "insert":
        index = int(command_data[1])
        value = command_data[2]
        l.insert(index, value)
    elif command_data[0] == "print":
        print(l)
    elif command_data[0] == "remove":
        l.remove(command_data[1])
    elif command_data[0] == "append":
        l.append(command_data[1])
    elif command_data[0] == "sort":
        l.sort()
    elif command_data[0] == "pop":
        l.pop()
    elif command_data[0] == "reverse":
        l.reverse()
    else:
        print("Unrecognised command please try again.")