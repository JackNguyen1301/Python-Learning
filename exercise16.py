#HÀM WHILE
x = int(input("Nhập số để tạo bảng cửu chương: "))

print(f"Bảng cửu chương của số {x}:")

i = 1
while i <= 10:
    r = x * i
    print(f"{x} x {i} = {r}")
    i+=1