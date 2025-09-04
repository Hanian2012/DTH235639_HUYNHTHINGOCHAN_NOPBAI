n = int(input("Nhập n: "))

tong = sum(range(1, n+1))
print("Tổng 1+2+...+n =", tong)

tong_le = sum(i for i in range(n) if i % 2 == 1)
tong_chan = sum(i for i in range(n) if i % 2 == 0)
print("Tổng số lẻ <", n, "=", tong_le)
print("Tổng số chẵn <", n, "=", tong_chan)
