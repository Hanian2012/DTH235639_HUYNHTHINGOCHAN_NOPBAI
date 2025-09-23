import random

# Nhập N
N = int(input("Nhập số lượng phần tử N: "))

# Sinh list N số ngẫu nhiên trong khoảng ví dụ từ 0 đến 100
lst = random.sample(range(0, 100), N)

print("List ngẫu nhiên không trùng nhau:", lst)
