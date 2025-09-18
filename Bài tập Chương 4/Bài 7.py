def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

arr = list(map(int, input("Nhập các số tự nhiên (cách nhau bởi khoảng trắng): ").split()))

odd = [x for x in arr if x % 2 == 1]
print("Dòng 1: Số lẻ:", odd, "Tổng cộng có", len(odd), "số lẻ")

even = [x for x in arr if x % 2 == 0]
print("Dòng 2: Số chẵn:", even, "Tổng cộng có", len(even), "số chẵn")

primes = [x for x in arr if is_prime(x)]
print("Dòng 3: Số nguyên tố:", primes, "Tổng cộng có", len(primes), "số nguyên tố")

not_primes = [x for x in arr if not is_prime(x)]
print("Dòng 4: Không phải số nguyên tố:", not_primes, "Tổng cộng có", len(not_primes), "số không nguyên tố")
