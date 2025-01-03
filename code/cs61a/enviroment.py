def square(x):
    return x * x


def triple(x):
    return x * 3


def compose1(f, g):
    def h(x):
        return f(g(x))

    return h


print(square(5))
print(triple(5))

squiple = compose1(square, triple)
print(squiple(5))

tripare = compose1(triple, square)
print(tripare(5))

print((lambda x: x * x)(5))


square = lambda x: x * x

print(repr(square))


def square(x):
    return x * x


print(repr(square))


def add(x, y, z):
    return x + y + z


def add(a):
    return lambda b: lambda c: a + b + c


# Usage
result = add(1)(2)(3)
print(result)
