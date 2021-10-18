n = input()
n = int(n)
while n < 2 or n > 10:
    print("Invalid number of users, please try again using a number between 2 and 10.")
    n = input()
    n = int(n)

d = {}
for i in range(0, n):
    invalid_grade = 3
    while invalid_grade != 0:
        details = input()
        details = details.split(" ")
        d[details[0]] = details[1:]
        for e in d[details[0]]:
            e_index = d[details[0]].index(e)
            d[details[0]][e_index] = int(d[details[0]][e_index])
            if d[details[0]][e_index] > 0 and d[details[0]][e_index] < 100:
                invalid_grade = invalid_grade - 1
        
        if invalid_grade != 0:
            print("You entered an invalid grade. Please try again using a number between 0 and 100")
            invalid_grade = 3

name = input()
average = 0
for grade in d[name]:
    average = average + grade
average = average / 3
print(average)