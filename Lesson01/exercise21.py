def xinchao(ho, chulot, ten):
    print("Xin chào:  " + ho + chulot + ten)

xinchao("Nguyễn", " Tấn", " Phú")
xinchao("Nguyễn", " Tấn", " Phúc")

def thu(*MonHoc):
    print("Thứ 2 học môn: " + MonHoc[0])
    print("Thứ 3 học môn: " + MonHoc[1])
    print("Thứ 4 học môn: " + MonHoc[2])
    print("Thứ 5 học môn: " + MonHoc[3])
    print("Thứ 6 học môn: " + MonHoc[4])

thu("Toan", "Ly", "Hoa", "Sinh", "Tieng Anh")

def tinhtong(*giatri):
    sum = 0
    for x in giatri:
        sum = sum + x
    print(sum)

tinhtong(1, 2, 3, 5)