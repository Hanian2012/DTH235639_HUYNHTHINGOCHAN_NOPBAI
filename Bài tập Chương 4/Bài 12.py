def combine_dict(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result

d1 = {'a': 100, 'b': 200}
d2 = {'a': 300, 'y': 200}
print("Combine:", combine_dict(d1, d2))
