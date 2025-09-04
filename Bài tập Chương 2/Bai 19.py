import math

def a(n):
    print("Tổng =", sum(range(1, n+1)))

def b(m, n):
    if math.gcd(m, n) == 1:
        print("Hai số nguyên tố cùng nhau")
    else:
        print("Không nguyên tố cùng nhau")

def c(s):
    h = s // 3600
    m = (s % 3600) // 60
    s = s % 60
    print(f"{h} giờ {m} phút {s} giây")

def d(a, b):
    print("Giá trị tuyệt đối =", abs(a-b))
