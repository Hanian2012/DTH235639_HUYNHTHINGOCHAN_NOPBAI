def doc_so(n):
    so_chu = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]

    if n < 10:  # số 1 chữ số
        return so_chu[n].capitalize()

    elif n < 20:  # từ 10 đến 19
        if n == 10:
            return "Muoi"
        elif n == 15:
            return "Muoi lam"
        else:
            return "Muoi " + so_chu[n % 10]

    else:  # từ 20 đến 99
        chuc = n // 10
        donvi = n % 10
        chuoi = so_chu[chuc].capitalize() + " muoi"

        if donvi == 0:
            return chuoi
        elif donvi == 1:
            return chuoi + " mot"
        elif donvi == 5:
            return chuoi + " lam"
        else:
            return chuoi + " " + so_chu[donvi]

# --- Chương trình chính ---
n = int(input("Nhap so n (0 <= n < 100): "))

if 0 <= n < 100:
    print("Cach doc:", doc_so(n))
else:
    print("Chi nhap so co toi da 2 chu so!")
