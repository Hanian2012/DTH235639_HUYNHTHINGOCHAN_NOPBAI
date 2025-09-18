d = {"a": 5, "b": 2, "c": 9, "d": 1}

asc = dict(sorted(d.items(), key=lambda item: item[1]))
desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print("Dictionary gốc:", d)
print("Sắp xếp tăng dần:", asc)
print("Sắp xếp giảm dần:", desc)
