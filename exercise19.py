import random
sdt = set()

while(True):
    print("-------MENU-------")
    print("1 - lựa chọn 1")
    print("2 - lựa chọn 2")
    print("3 - lựa chọn 3")
    print("4 - lựa chọn 4")
    print("sdt hiện tại: ")
    print(sdt)

    luachon = int(input("Nhập vào số: "))

    if (luachon==1):
         print("Chúc mừng bạn may mắn lần sau: ")

    elif (luachon==2):
        r = input("Nhập số điện thoại để nhận thưởng: ")
        sdt.add(r) 

    elif (luachon==3):
        t = input("Nhập số điện thoại cần xóa: ")
        sdt.discard(t)

    elif (luachon==4):
        index = random.randint(0,len(sdt)-1)
        print("Vị trí trúng thưởng: " + str(index))

        i = 0
        for x in sdt:
            if(i==index):
                print("Chúc mừng SĐT: Số " +  x + " Đã trúng thưởng!")
                sdt.discard(x)
            i=i+1
    else:
        continue
        
        f = input("Nhập phím bất kì để tiếp tục: ")

     

         
