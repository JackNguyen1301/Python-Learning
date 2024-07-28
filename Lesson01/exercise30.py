try:
    with open(r"C:\Users\Phu Nguyen\OneDrive\Documents\test.txt", "wt") as f:
        content = f.write("Hello World")
except FileNotFoundError:
    print("Không tìm thấy file")