#HÀM FOR 
content = input("Nhập nội dung: ")
x = int(input("Nhập vào số: "))
for i in range(x):
    print(i+1, ". ", content)

number = int(input("Nhập số để tạo bản cửu chương: "))
print("Bảng cửu chương của số: ",number)
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

