n = int(input("Nhập n: "))

S = sum(range(1, n+1))
S1 = sum(2*i - 1 for i in range(1, n+1))
S2 = sum(2*i for i in range(1, n+1))
S3 = sum(i**2 for i in range(1, n+1))
S4 = sum(1/i for i in range(1, n+1))

print("S =", S)
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
