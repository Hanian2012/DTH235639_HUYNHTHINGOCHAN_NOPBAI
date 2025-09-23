def toi_uu_chuoi(s):
    # Xóa khoảng trắng dư thừa 2 đầu, tách các từ
    words = s.strip().split()
    # Viết hoa chữ cái đầu mỗi từ
    words = [w.capitalize() for w in words]
    # Ghép lại thành chuỗi
    return " ".join(words)

# Nhập chuỗi từ bàn phím
chuoi = input("Nhập chuỗi: ")
print("Chuỗi tối ưu:", toi_uu_chuoi(chuoi))
