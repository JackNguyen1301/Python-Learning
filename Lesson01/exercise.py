try:
    with open(r"C:\Users\Phu Nguyen\OneDrive\Documents\test.txt", "w") as f:
        f.write(input("Nhập vào dữ liệu: "))
    f = open(r"C:\Users\Phu Nguyen\OneDrive\Documents\test.txt", "r")
    content = f.read()
    print("Dữ liệu: ", content)
        
except FileNotFoundError:
    print("file không tồn tại")