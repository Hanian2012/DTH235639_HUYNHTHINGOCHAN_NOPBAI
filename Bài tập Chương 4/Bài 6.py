import random

def create_random_list(n, start=0, end=100):
    return [random.randint(start, end) for _ in range(n)]

def remove_value(lst, value):
    return [x for x in lst if x != value]

def is_symmetric(lst):
    return lst == lst[::-1]


lst = create_random_list(10, 1, 9)
print("List ngẫu nhiên:", lst)

value = lst[0]
lst = remove_value(lst, value)
print(f"Sau khi xóa tất cả {value}:", lst)

print("Có đối xứng không?", is_symmetric(lst))
