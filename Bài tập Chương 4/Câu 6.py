import random
values = [4.5, 34, -1, 100, 0, 99]
def check_values(values):
    possible_values = set(range(0, 100))  
    for v in values:
        if v in possible_values:
            print(f"{v} -> Có thể xuất hiện")
        else:
            print(f"{v} -> Không thể xuất hiện")
check_values(values)
print("\nVí dụ 10 số random từ randrange(0,100):")
for i in range(10):
    print(random.randrange(0, 100), end=" ")
