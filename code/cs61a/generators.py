def evens(start, end):
    # 2 = 1 + 1%2
    even = start + (start % 2)
    while even <= end:
        yield even
        even += 2


print(list(evens(1, 10)))

t = evens(2, 10)
print(next(t))
print(next(t))
