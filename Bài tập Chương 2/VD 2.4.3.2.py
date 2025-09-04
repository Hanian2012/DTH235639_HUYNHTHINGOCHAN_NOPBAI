#Chương trình minh họa sử dụng lệnh continue
a = 10
while(a > 0):
    a = a - 1
    if (a == 5): #kiểm tra số lẻ
        continue #bỏ qua các câu lệnh bên dưới trong vòng lặp
    print('Giá trị biến hiện tại là: ', a)
print('Kêt thúc...')
