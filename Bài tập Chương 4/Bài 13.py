def evaluate_polynomial(coeffs, x):
    result = 0
    for i, a in enumerate(coeffs):
        result += a * (x ** i)
    return result
coeffs = [int(i) for i in input("Nhập các hệ số a0,a1,...,an (cách nhau bởi dấu cách): ").split()]
x = int(input("Nhập giá trị x: "))
print("Giá trị của đa thức:", evaluate_polynomial(coeffs, x))