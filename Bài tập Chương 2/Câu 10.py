# Ví dụ minh họa các lệnh viết ngắn gọn trong Python

x = 10
y = 3
ncc = 4
number_of_closed_cases = 5

print("Giá trị ban đầu:")
print("x =", x, "y =", y, "ncc =", ncc, "number_of_closed_cases =", number_of_closed_cases)

# (a) x = x + 1
x += 1
print("(a) x += 1  →", x)

# (b) x = x / 2
x /= 2
print("(b) x /= 2  →", x)

# (c) x = x - 1
x -= 1
print("(c) x -= 1  →", x)

# (d) x = x + y
x += y
print("(d) x += y  →", x)

# (e) x = x - (y + 7)
x -= (y + 7)
print("(e) x -= (y + 7)  →", x)

# (f) x = 2 * x
x *= 2
print("(f) x *= 2  →", x)

# (g) number_of_closed_cases = number_of_closed_cases + 2*ncc
number_of_closed_cases += 2 * ncc
print("(g) number_of_closed_cases += 2 * ncc  →", number_of_closed_cases)
