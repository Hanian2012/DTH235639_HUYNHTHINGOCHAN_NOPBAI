def yody_sales():
    sales = []
    for i in range(10):
        val = float(input(f"Nhập doanh số cửa hàng {i+1}: "))
        sales.append(val)

    print("Danh sách doanh số:", sales)

    sorted_sales = sorted(sales)
    print("Doanh số sắp xếp tăng dần:", sorted_sales)

    avg_sales = sum(sales) / len(sales)
    print("Trung bình doanh số:", avg_sales)

    max_sales = max(sales)
    max_index = sales.index(max_sales) + 1
    print(f"Cửa hàng có doanh số cao nhất: Cửa hàng {max_index} với {max_sales}")

yody_sales()
