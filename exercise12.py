#TOÁN TỬ ĐIỀU KIỆN
x = input("Nhập vào số: ")
x = int(x)

kq = "Đúng" if (x < 100) else "Sai"
print (x, "nhỏ hơn 1000:" ,kq)

r = input("Nhập vào số nguyên: ")
r = int(r)

y = "Chẵn" if (r%2==0) else "Lẻ"
print(r, y)