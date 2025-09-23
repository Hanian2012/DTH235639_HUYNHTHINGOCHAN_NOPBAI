import os

# Hàm lấy tên file có đuôi
def get_filename_with_ext(path):
    return os.path.basename(path)

# Hàm lấy tên file không có đuôi
def get_filename_without_ext(path):
    return os.path.splitext(os.path.basename(path))[0]

# Chạy thử
duong_dan = input("Nhập đường dẫn file nhạc: ")

print("Tên file có đuôi:", get_filename_with_ext(duong_dan))
print("Tên file không có đuôi:", get_filename_without_ext(duong_dan))
