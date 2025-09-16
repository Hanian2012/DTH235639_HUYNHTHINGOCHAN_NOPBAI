import math

xA, yA = map(float, input("Nhập tọa độ A(xA, yA): ").split())
xB, yB = map(float, input("Nhập tọa độ B(xB, yB): ").split())

d = math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)

print(f"Độ dài AB = {d:.2f}")
