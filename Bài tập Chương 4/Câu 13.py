def sum_divisors(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s

def is_perfect(n):
    return sum_divisors(n) == n

def is_abundant(n):
    return sum_divisors(n) > n

n = int(input("Nhập số nguyên dương n: "))

if is_perfect(n):
    print(f"{n} là số hoàn thiện")
else:
    print(f"{n} không phải số hoàn thiện")

if is_abundant(n):
    print(f"{n} là số thịnh vượng")
else:
    print(f"{n} không phải số thịnh vượng")
