n = int(input('Nhập số n: '))
s = 0
for i in range(1,n):
    if n % i == 0:
        s = s + i
    if s == n:
        print(n, 'là số hoàn hảo')
    else:
        print(n, 'không phải là số hoàn hảo')