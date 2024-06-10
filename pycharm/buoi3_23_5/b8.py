print("đề 8: viết chương trình chuyển đổi từ km sang mm và ngược lại")

while True:
    print("chọn loại chuyển đổi")
    print("1: km sang mm")
    print("2: mm sang km")
    print("3: thoát")

    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        km = float(input("Nhập vào số km: "))
        mm = km * 1000
        print("Số mm là: ", mm)
    elif choice == "2":
        mm = float(input("Nhập vào số mm: "))
        km = mm / 1000
        print("Số km là: ", km)
    elif choice == "3":
        break
    else:
        print("Lựa chọn không hợp lệ")