n = int(input("Nhập n: "))

# a) Số ước số nguyên tố khác nhau
def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

uoc_nguyen_to = [i for i in range(2, n+1) if n % i == 0 and is_prime(i)]
print("Ước nguyên tố:", uoc_nguyen_to)

# b) Tổng các ước số tự nhiên
tong_uoc = sum(i for i in range(1, n+1) if n % i == 0)
print("Tổng ước số:", tong_uoc)

# c) Tổng 12+22+...+n2
tong_binh_phuong = sum(i**2 for i in range(1, n+1))
print("Tổng bình phương:", tong_binh_phuong)
