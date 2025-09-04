def bar(a):
    a = a - 1
    return a
def foo(a):
    a = a * a
    b = bar(a)
    return b
def main():
    x = 2
    y = foo(x)
    print('x =', x)
    print('y =', y)
main()