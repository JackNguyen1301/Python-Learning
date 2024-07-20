tudien = {}
while(True):
    try:
        print("------------MENU------------")
        print("VUI LÒNG LỰA CHON CHỨC NĂNG BẰNG SỐ")
        print("LỰA CHỌN 1. Thêm một từ vựng mới, kèm theo ý nghĩa của từ vừng đó.")
        print("LỰA CHỌN 2. Tra cứu từ vựng.")
        print("LỰA CHỌN 3. Cập nhật một ý nghĩa mới cho 1 từ vựng.") 
        print("LỰA CHỌN 4. Cho phép người dùng xóa đi một từ vựng.")
        print("LỰA CHON 5. Cho phép người dùng xoa toàn bộ dữ liệu.")
        print("LỰA CHỌN 6. Cho phép người dùng in tất cả dữ liệu.")
        print("LỰA CHON 7. Cho phép người dung in ra tất cả từ vựng theo tên và ý nghĩa.")
        print("LỤA CHỌN 8. Kết thúc chương trình.")
        luachon = int(input("Nhập vào lựa chọn của bạn: "))
        if (luachon == 1):
            tuvung = input("Nhập vào từ vựng: ")
            ynghia = input("Nhập vào ý nghĩa: ")
            tudien[tuvung] = ynghia
            print("Đã cập nhật dữ liệu!")
        elif (luachon == 2):
            tuvung = input("Nhập vào từ vựng: ")
            print("Ý nghĩa: ", tudien[tuvung])
            
        elif (luachon == 3):
            tuvung = input("Nhập vào từ vựng: ")
            ynghia = input("Nhập vào ý nghĩa: ")
            tudien[tuvung] = ynghia
            print("Đã cập nhật dữ liệu")
        elif (luachon == 4):
            tuvung = input("Nhập vào từ vựng: ")
            tudien.pop(tuvung)
            print("Đã xóa dữ liệu!")
        elif (luachon == 5):
            tuvung.clear()
            print("Đã xóa toàn bộ dữ liệu!")
        elif (luachon == 6):
            print("DANH SÁCH CÁC TỪ VỰNG")
            for x in tudien.keys():
                print(x)
        elif (luachon == 7):
            for r, y in tudien.items():
                print(r, ":", y) 
        elif (luachon == 8):
            print("Kết thúc chương trình.")
            break;
        else:
            print("Nhập lựa chọn không đúng! ")   
    except:
        print("Không có từ vựng này.")
        continue