def nhap_day_tang(n):
    lst = []
    for i in range(n):
        while True:
            x = int(input(f"Nhập số thứ {i+1}: "))
            if i == 0 or x > lst[-1]:
                lst.append(x)
                break
            else:
                print("Sai quy cách! Phải nhập lớn hơn số trước đó. Nhập lại...")
    return lst

# Chương trình chính
n = int(input("Nhập số lượng phần tử: "))
day_so = nhap_day_tang(n)

print("Dãy số tăng dần đã nhập:", day_so)
