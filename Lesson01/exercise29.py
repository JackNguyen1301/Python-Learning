try:
    with open(r"C:\Users\Phu Nguyen\AppData\Local\Packages\Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe\LocalState\{e06adece-2113-4c3e-b6a9-08e7a01a6a30}\Capture0.png", "rb") as f:
        data = f.read()
except FileNotFoundError:
    print("file không tồn tại")