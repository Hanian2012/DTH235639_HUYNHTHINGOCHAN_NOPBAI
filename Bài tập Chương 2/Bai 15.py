a, b, c = map(float, input("Nhập 3 cạnh a, b, c: ").split())

if a + b > c and a + c > b and b + c > a:
    print("Có thể tạo thành tam giác")
else:
    print("Không thể tạo thành tam giác")
