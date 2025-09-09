def test_case(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print("i =", i, ", j =", j, ", k =", k)


# Các trường hợp đề bài
print("a) i=3, j=5, k=7")
test_case(3, 5, 7)

print("b) i=3, j=7, k=5")
test_case(3, 7, 5)

print("c) i=5, j=3, k=7")
test_case(5, 3, 7)

print("d) i=5, j=7, k=3")
test_case(5, 7, 3)

print("e) i=7, j=3, k=5")
test_case(7, 3, 5)

print("f) i=7, j=5, k=3")
test_case(7, 5, 3)
