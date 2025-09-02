a = int(input('Nhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print('Ước chung lớn nhất của a và b là: ', a)