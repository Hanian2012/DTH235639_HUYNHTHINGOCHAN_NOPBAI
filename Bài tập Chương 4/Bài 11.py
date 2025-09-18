def merge_dict(d1, d2):
    d1.update(d2)
    return d1
d1 = {'a': 100, 'b': 200}
d2 = {'a': 300, 'y': 200}
print("Merge:", merge_dict(d1.copy(), d2))