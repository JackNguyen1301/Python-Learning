while True:
    print("Vui lòng lựa chọn hình bạn muốn tính")
    print("1. Tính chu vi hình vuông")
    print("2. Tính chu vi hình chữ nhật")
    print("3. Tính chu vi hình tam giác")
    print("4. Tính diện tích hình vuông")
    print("5. Tính diện tích hình chữ nhật")
    print("6. Tính diện tích hình tam giác")
    print("Ấn số 0 để thoát")

    luachon = int(input("Nhập vào lựa chọn của bạn: "))

    if luachon == 1:
        d = int(input("Nhập vào cạnh: "))
        kq = d * 4
        print("Chu vi hình vuông là:", kq)
    elif luachon == 2:
        dai = int(input("Nhập vào chiều dài: "))
        rong = int(input("Nhập vào chiều rộng: "))
        kq = 2 * (dai + rong)
        print("Chu vi hình chữ nhật là:", kq)
    elif luachon == 3:
        a = int(input("Nhập vào cạnh a: "))
        b = int(input("Nhập vào cạnh b: "))
        c = int(input("Nhập vào cạnh c: "))
        kq = a + b + c
        print("Chu vi hình tam giác là:", kq)
    elif luachon == 4:
        d = int(input("Nhập vào cạnh: "))
        kq = d * d
        print("Diện tích hình vuông là:", kq)
    elif luachon == 5:
        dai = int(input("Nhập vào chiều dài: "))
        rong = int(input("Nhập vào chiều rộng: "))
        kq = dai * rong
        print("Diện tích hình chữ nhật là:", kq)
    elif luachon == 6:
        day = int(input("Nhập vào đáy: "))
        cao  = int(input("Nhập vào chiều cao: "))
        kq = 0.5 * day * cao  
        print("Diện tích hình tam giác là:", kq)
    elif luachon ==0:
        print("Chương trình đã kết thúc")
        break
    
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")