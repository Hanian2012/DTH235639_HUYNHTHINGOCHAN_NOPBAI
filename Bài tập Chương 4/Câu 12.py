def oscillate(start, k):
    for i in range(start, 1):  # từ start đến 0
        yield i
        yield -i
    yield 0
    yield 0
    for i in range(1, k):
        yield i
        yield -i

for n in oscillate(-3, 5):
    print(n, end=' ')

