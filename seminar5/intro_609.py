# this is a line comment

"""
This is a multi line comment.
Everything I add here will be considered a comment.
The interpreter ignores all comments.
They are there for us to explain our code.
"""

n = input("Please enter a number: ")  # this is an inline comment
print(type(n), n)

n = int(n)
print(type(n), n)

# n = float(n)
# print(type(n), n)

s = "andrei 10 10 10"
s = s.split(" ")
print(s)

rest = 15 % 6
print(rest)

if n % 2 == 0:
    n1 = n * 2
    n2 = n * 3
    print(f'{n} is even')
    print(f'double of {n} = {n1}')
    print(f'triple of {n} = {n2}')
else:
    print(f'{n} is odd')

for i in range(10):
    i2 = i * 2
    print(f'i = {i}')
    print(f'double i = {i2}')
    if i % 2 == 1:
        print(f'{i} is odd')

print(f'Done!')

# `this is a ${n}`
text = f'This is a string where I add the value of a variable. Variable n = {n}. Variable s = {s}'
print(text)

