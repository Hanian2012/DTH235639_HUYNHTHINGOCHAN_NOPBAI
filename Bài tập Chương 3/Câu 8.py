# Nhập vào 2 số và phép toán
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
pheptoan = input("Nhập phép toán (+, -, *, /): ")

# Xử lý phép toán
if pheptoan == "+":
    ketqua = a + b
elif pheptoan == "-":
    ketqua = a - b
elif pheptoan == "*":
    ketqua = a * b
elif pheptoan == "/":
    if b != 0:
        ketqua = a / b
    else:
        ketqua = "Lỗi: Không thể chia cho 0!"
else:
    ketqua = "Phép toán không hợp lệ!"

# Xuất kết quả
print("Kết quả:", ketqua)
