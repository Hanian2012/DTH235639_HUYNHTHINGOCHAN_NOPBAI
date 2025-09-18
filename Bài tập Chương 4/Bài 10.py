def concat_dict(d1, d2):
    return {**d1, **d2}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
print("Concat:", concat_dict(dic1, dic2))