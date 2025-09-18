def gen_even(n):
    count = 0
    num = 0
    while count < n:
        yield num
        num += 2
        count += 1
print("5 số chẵn đầu tiên:", list(gen_even(5)))
def gen_square(n):
    count = 0
    num = 0
    while count < n:
        yield num * num
        num += 1
        count += 1
print("5 số chính phương đầu tiên:", list(gen_square(5)))