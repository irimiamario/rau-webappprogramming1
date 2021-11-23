def simple_sum(a: int, b: int) -> int:
    return a + b


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, str):
            a1 = self.a + int(other)
            result = A(a1, self.b)
        else:
            a1 = self.a + other.a
            b1 = self.b + other.b
            result = A(a1, b1)
        return result

    def __sub__(self, other):
        o = A(-other.a, -other.b)
        return self.__add__(o)


class B(A):
    def __init__(self, a, b):
        super().__init__(a, b)

    def __sub__(self, other):
        o = B(-other.a, other.b)
        return self.__add__(o)


r1 = simple_sum(1, 2)
print(f"Result 1 = {r1}")
r2 = simple_sum('a', 'b')
print(f"Result 2 = {r2}")

a1 = A(10, 20)
a2 = A(20, 20)

r3 = simple_sum(a1, a2)
print(f"Result 3 = ({r3.a}, {r3.b})")

r4 = simple_sum(a1, '2090')
print(f"Result 4 = ({r4.a}, {r4.b})")

print(a1 - a2)

b1 = B(10, 10)
b2 = B(10, 100)

r5 = b1 - b2
print(f"Result 5 = ({r5.a}, {r5.b})")
