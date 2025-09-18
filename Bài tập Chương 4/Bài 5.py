def create_list():
    return []

def add_element(lst, value):
    lst.append(value)

def count_occurrences(lst, value):
    return lst.count(value)

def sum_list(lst):
    return sum(lst)

def sort_list(lst):
    lst.sort()

def delete_list(lst):
    lst.clear()

my_list = create_list()
add_element(my_list, 5)
add_element(my_list, 3)
add_element(my_list, 5)
print("List:", my_list)
print("Số lần xuất hiện của 5:", count_occurrences(my_list, 5))
print("Tổng:", sum_list(my_list))
sort_list(my_list)
print("Sau sắp xếp:", my_list)
delete_list(my_list)
print("Sau khi xóa:", my_list)
