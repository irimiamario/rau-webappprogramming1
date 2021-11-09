def product(n):
    p = 1
    for i in range(2, n+1):
        p = p * i
    return p


def sum_(a, b, c):
    s = a + b - c
    return s


def function_with_variable_args(t, *args, **kwargs):
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")
    print(f"args[0] = {args[0]}")
    print(f"kwargs['a'] = {kwargs['a']}")


p1 = product(10)
print(f"Product up to and including {10} is {p1}")

s1 = sum_(1, 2, 3)
print(f"s1 = {s1}")

s2 = sum_(b=1, c=2, a=3)
print(f"s2 = {s2}")

function_with_variable_args(1, 2, 3, 4, a=1, b=20, c=30)


def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)



