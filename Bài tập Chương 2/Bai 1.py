so_tien = float(input("Nhập số tiền gốc ban đầu: "))
lai_suat = 0.006  # 0.6%/tháng
thang = 18

for i in range(thang):
    so_tien += so_tien * lai_suat

print("Số tiền nhận được sau 18 tháng là:", "{:,.2f}".format(so_tien))