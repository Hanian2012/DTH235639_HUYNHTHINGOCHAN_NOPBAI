from datetime import datetime, timedelta

# Nhập ngày/tháng/năm
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

try:
    # Tạo đối tượng ngày
    d = datetime(nam, thang, ngay)

    # Cộng thêm 1 ngày
    ngay_ke_tiep = d + timedelta(days=1)

    # In kết quả
    print("Ngày kế tiếp là:", ngay_ke_tiep.day, "/", ngay_ke_tiep.month, "/", ngay_ke_tiep.year)

except ValueError:
    print("Ngày tháng năm không hợp lệ!")
