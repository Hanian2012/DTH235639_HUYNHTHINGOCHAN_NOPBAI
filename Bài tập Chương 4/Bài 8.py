def sum_dict(d):
    return sum(d.values())

def product_dict(d):
    result = 1
    for v in d.values():
        result *= v
    return result

d = {"a": 2, "b": 3, "c": 4}

print("Tổng các giá trị:", sum_dict(d))
print("Tích các giá trị:", product_dict(d))
