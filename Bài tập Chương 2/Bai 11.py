import math

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0
for i in range(n+1):
    S += x**i / math.factorial(i)

print("Kết quả S =", S)
