n = int(input('Nhập n: '))
for x in range(1,n,1):
    if x % 2 == 0:
        continue
    print('x= ',x,' là số lẻ')