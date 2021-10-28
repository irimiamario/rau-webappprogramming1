# for
l1 = [1, 2, 3, 4, 6]
for e in l1:
    a = e ** 3
    print(a)

print("Done!")

for i, e in enumerate(l1):
    if i > 2:
        print(i, e)

s = 0
for i in range(0, 100):
    s = s + i
print(f"Average of the first 99 numbers: {s / 99}")

# while
# while condition:
#   statements
n = 0
# while n < 2 or n > 10:
#     print("Please enter a number between 2 and 10")
#     n = input()
#     n = int(n)
# print("Done!")

# while True:
#     n = input()
def sum_numbers(n, p=0):
    s = 0
    for i in range(0, n):
        s = s + i
    print(f"Sum of the first {n-1} numbers is {s}.")
    return s

def sum_numbers_raised(n, p=2):
    s = 0
    for i in range(0, n):
        s = s + i ** p
    print(f"Sum of the first {n-1} numbers raised to the power of {p} is {s}.")
    return s

a = sum_numbers(10)
b = sum_numbers(n=20, p=100)

function_label = sum_numbers
function_label(10)

l = [sum_numbers, sum_numbers_raised]
for f in l:
    f(10, p=10)

def power(a, b):
    return a ** b

def sample(a, b):
    return 1

def sum_numbers_raised_to_power(n, p, f):
    s = 0
    for i in range(0, n):
        s = s + f(i, p)
    print(f"Sum of the first {n-1} numbers raised to the power of {p} is {s}.")
    return s

sum_numbers_raised_to_power(10, 2, power)
sum_numbers_raised_to_power(10, 2, sample)

def modify_string(s):
    s = s
    def inside_function():
        return s + "_suffix"
    return inside_function

f = modify_string("abc")
print(f)
print(f())

from datetime import datetime

def my_decorator(func):
    def wrapper():
        print("This is happening before we call func")
        if 7 <= datetime.now().hour <= 22:
            func()
            func()
        else:
            print("Everyone is sleeping. Leave me alone.")
        print("This is happening after we call func")
    return wrapper

@my_decorator
def hello():
    print("Hello World!")

hello()

f = lambda x, y: x + y
print(f(1,2))

l = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda x: x % 2 == 0, l)
pow2 = map(lambda x: x ** 2, l)
print(list(pow2))

def is_even(x):
    return x % 2 == 0

evens2 = filter(is_even, l)
print(list(evens2))

uppercase = map(lambda x: x.upper(), "abcdefg")
print(list(uppercase))