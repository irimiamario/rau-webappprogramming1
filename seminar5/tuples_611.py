n = input("Please enter a number: ")
n = int(n)

numbers = input(f"Please enter {n} numbers separated by space: ")
numbers = numbers.split(" ")

for idx in range(n):
    numbers[idx] = int(numbers[idx])

t1 = tuple(numbers)
hash_t1 = hash(t1)

print(f"Hash for {t1} is {hash_t1}")

t2 = (1, 2, 3)
hash_t2 = hash(t2)
print(f"Hash for {t2} is {hash_t2}")

print(hash_t1 == hash_t2)

variabila1 = [1, 2, 3]
variabila11 = list([1, 2, 3])
variabila2 = (1, 2, 3)
variabila21 = tuple([1, 2, 3])
variabila3 = {1, 2, 3}
variabila31 = set([1, 2, 3])
variabila4 = {
    1: 1,
    2: 2,
    3: 3
}
variabila41 = dict(value=1, other_value=2)

n_t1 = len(t1)
n_t2 = len(t2)
if n_t1 != n_t2:
    print(False)
else:
    for i in range(n_t1):
        if t1[i] != t2[i]:
            print(False)

hash_t1 = hash(t1)
hash_t2 = hash(t2)
print(hash_t1 == hash_t2)
