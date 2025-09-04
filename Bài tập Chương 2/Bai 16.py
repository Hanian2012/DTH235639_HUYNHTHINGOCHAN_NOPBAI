day, month, year = map(int, input("Nhập ngày, tháng, năm: ").split())

hop_le = True
if month < 1 or month > 12:
    hop_le = False
elif day < 1 or day > 31:
    hop_le = False
elif month in [4, 6, 9, 11] and day > 30:
    hop_le = False
elif month == 2:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        if day > 29: hop_le = False
    else:
        if day > 28: hop_le = False

print("Ngày hợp lệ" if hop_le else "Ngày không hợp lệ")
