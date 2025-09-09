canh = int(input("Nhập độ dài cạnh hình vuông: "))
for i in range(canh):
    if i == 0 or i == canh - 1:
        print('* ' * canh)
    else:
        print('* ' + '  ' * (canh - 2 )+ '*')

chieu_cao = int(input("Nhập chiều cao tam giác: "))
for i in range(1, chieu_cao + 1):
    print('  ' * (chieu_cao - i) + '* ' * i)

print("\nHình tam giác vuông có 2 đỉnh chạm nhau:")
rows = 7  # số dòng

for i in range(rows):
    if i == 0:
        print("*")                    # dòng đầu có 1 *
    elif i == 1:
        print("* "," " * (i-1), "*", sep="")   # dòng 2 có 2 *
    elif i == 2:
        print("*  ", " " * (i-1), "*", sep="")   # dòng 3 có 2 *
    elif i == 3:
        print("* " * 7)                # dòng ngang dài
    elif i == 4:
        print(" " * (i+1), "  *   *")        # dòng 5 có 2 *
    elif i == 5:
        print(" " * (i+2), "  * *")         # dòng 6 có 2 *
    elif i == 6:
        print(" " * (i+3), "  *")          # dòng cuối có 1 *