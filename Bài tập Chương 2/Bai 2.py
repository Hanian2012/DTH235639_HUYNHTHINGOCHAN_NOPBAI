a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
op = input("Nhập phép toán (+, -, *, /): ")

if op == "+":
    print("Kết quả:", a + b)
elif op == "-":
    print("Kết quả:", a - b)
elif op == "*":
    print("Kết quả:", a * b)
elif op == "/":
    if b != 0:
        print("Kết quả:", a / b)
    else:
        print("Không thể chia cho 0")
else:
    print("Ký tự nhập không hợp lệ")
