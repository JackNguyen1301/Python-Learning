
def ktsochan (num):
    if (num%2==0):
        return("Số chẵn")
    else:
        return("Số lẻ")
x = int(input("Nhập vào số: "))
print(ktsochan(x))