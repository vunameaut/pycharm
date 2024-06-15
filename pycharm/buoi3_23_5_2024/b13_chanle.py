print("b13: Nhập vào một danh sách và cho biết danh sách đó có bao nhiêu số lẻ và số chẵn?")

numbers = input("nhap vao danh sách : ").split()

sochan = 0

sole = 0

for i in numbers:
    i = int(i)
    if i % 2 == 0:
        sochan += 1
    else:
        sole += 1

print("so chan la: ", sochan)

print("so le la: ", sole)
