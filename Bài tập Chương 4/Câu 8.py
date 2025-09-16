import math

x = float(input("Nhập x (>0): "))
a = float(input("Nhập a (>0, a != 1): "))

if x > 0 and a > 0 and a != 1:
    result = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {result}")
else:
    print("Điều kiện không hợp lệ (x > 0, a > 0, a != 1)")
