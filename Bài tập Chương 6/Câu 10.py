def nhap_matrix(rows, cols, name):
    print(f"Nhập ma trận {name}:")
    M = []
    for i in range(rows):
        row = list(map(int, input(f"Hàng {i+1}: ").split()))
        while len(row) != cols:
            print("Số phần tử không khớp, nhập lại!")
            row = list(map(int, input(f"Hàng {i+1}: ").split()))
        M.append(row)
    return M

def cong_matrix(A, B):
    rows, cols = len(A), len(A[0])
    C = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return C

def hoan_vi_matrix(M):
    rows, cols = len(M), len(M[0])
    T = [[M[j][i] for j in range(rows)] for i in range(cols)]
    return T

def xuat_matrix(M, name):
    print(f"Ma trận {name}:")
    for row in M:
        print(row)
    print()

# --- Chương trình chính ---
rows = int(input("Nhập số hàng: "))
cols = int(input("Nhập số cột: "))

A = nhap_matrix(rows, cols, "A")
B = nhap_matrix(rows, cols, "B")

# Xuất ma trận A, B
xuat_matrix(A, "A")
xuat_matrix(B, "B")

# Cộng 2 ma trận
C = cong_matrix(A, B)
xuat_matrix(C, "A + B")

# Hoán vị A và B
TA = hoan_vi_matrix(A)
TB = hoan_vi_matrix(B)
xuat_matrix(TA, "A^T (hoán vị)")
xuat_matrix(TB, "B^T (hoán vị)")
