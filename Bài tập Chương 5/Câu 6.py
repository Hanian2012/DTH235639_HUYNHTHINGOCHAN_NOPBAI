import re

def NegativeNumberInStrings(s):
    # Dùng regex để tìm tất cả số âm: dấu '-' đi trước 1 hoặc nhiều chữ số
    numbers = re.findall(r'-\d+', s)
    # Chuyển về số nguyên
    result = [int(num) for num in numbers]
    return result

# Chạy thử
chuoi = "abc-5xyz-12k9l--p"
print("Chuỗi:", chuoi)
print("Các số nguyên âm trong chuỗi:", NegativeNumberInStrings(chuoi))
