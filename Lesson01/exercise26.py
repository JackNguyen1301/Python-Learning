try:
    f = open(r"c:\test.txt", "r")
    content = f.read()
    print(content)

except FileNotFoundError:
    print("File không tồn tại. ")       
finally:
    f.close
    