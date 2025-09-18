class ThiSinh:
    def __init__(self, so_bao_danh, ho_ten, diem_toan, diem_van):
        self.so_bao_danh = so_bao_danh
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_van = diem_van
        self.tong_diem = diem_toan + diem_van

    def __str__(self):
        return f"{self.so_bao_danh}\t{self.ho_ten}\tToán: {self.diem_toan}\tVăn: {self.diem_van}\tTổng: {self.tong_diem}"


def main():
    ds = []
    n = int(input("Nhập số lượng thí sinh: "))
    for i in range(n):
        so_bao_danh = input("Số báo danh (5 ký tự): ")
        ho_ten = input("Họ và tên: ")
        diem_toan = float(input("Điểm Toán: "))
        diem_van = float(input("Điểm Văn: "))
        ds.append(ThiSinh(so_bao_danh, ho_ten, diem_toan, diem_van))

    print("\nDanh sách thí sinh:")
    for ts in ds:
        print(ts)

    print("\nDanh sách thí sinh có tổng điểm > 10:")
    for ts in ds:
        if ts.tong_diem > 10:
            print(ts)

    print("\nDanh sách thí sinh có điểm liệt:")
    for ts in ds:
        if ts.diem_toan == 0 or ts.diem_van == 0:
            print(ts)


main()
