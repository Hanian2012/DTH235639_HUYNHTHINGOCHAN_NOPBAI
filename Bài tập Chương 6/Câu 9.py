def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# Dòng 1: số lẻ
le = [x for x in M if x % 2 != 0]
print("Số lẻ:", le, "→ Tổng cộng:", len(le))

# Dòng 2: số chẵn
chan = [x for x in M if x % 2 == 0]
print("Số chẵn:", chan, "→ Tổng cộng:", len(chan))

# Dòng 3: số nguyên tố
nt = [x for x in M if la_nguyen_to(x)]
print("Số nguyên tố:", nt)

# Dòng 4: số không nguyên tố
khong_nt = [x for x in M if not la_nguyen_to(x)]
print("Không phải nguyên tố:", khong_nt)
