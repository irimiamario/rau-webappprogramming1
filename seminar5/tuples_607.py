n = input("Enter how many numbers you want to read ")
n = int(n)

numbers = input()
numbers = numbers.split(" ")

wanted_numbers = []
for i in range(n):
    wanted_number = int(numbers[i])
    wanted_numbers.append(wanted_number)

t = tuple(wanted_numbers)
hash_t = hash(t)

print(f"Hash of {t} is {hash_t}.")
