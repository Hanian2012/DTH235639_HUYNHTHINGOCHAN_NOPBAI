thang = int(input("Nhập tháng (1-12): "))

if thang in [1, 3, 5, 7, 8, 10, 12]:
    print("Tháng có 31 ngày")
elif thang in [4, 6, 9, 11]:
    print("Tháng có 30 ngày")
elif thang == 2:
    nam = int(input("Nhập năm: "))
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        print("Tháng 2 có 29 ngày (năm nhuận)")
    else:
        print("Tháng 2 có 28 ngày")
else:
    print("Tháng không hợp lệ")
