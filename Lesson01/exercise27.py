try:
    with open(r"C:\Users\Phu Nguyen\OneDrive\Documents\test.txt", "w") as f:
        f.write(input("Nhập vào dữ liệu: "))
        f.close()
except FileNotFoundError:
    print("file không tồn tại")