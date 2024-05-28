from ntpath import join
import os
import random
import shutil


def cau1():
    file_name = str(input("Nhập tên file muốn tạo: "))
    file=open(file_name, "w")
    list = random.sample(range(1,100), 10)
    file.write("".join(map(str,list)))
    file.close()
    filer=open(file_name, "r")
    print(filer.read())
    filer.close()

def cau2():
    file_name = input("Nhập tên file muốn tạo: ")
    file=open(file_name, "w")
    write = input("Nhập nội dung muốn ghi vào file: ")
    file.write(write)
    file.close()
    fileo=open(file_name, "r")
    print(fileo.read())
    fileo.close()

def cau3():
    a= int(input("nhap vao gia tri cua a: "))
    for i in range(1,11):
        file = open("bangcuuchuong.txt", "w")
        for i in range(1,11):
            file.write(str(a) + "*" + str(i) + "=" + str(a*i) + "\n")
    file.close()

def cau4():
    file_goc = str(input("Nhập tên file gốc: "))
    fileg=open(file_goc, "r")
    noidung = fileg.read()
    fileg.close()

    file_new = str(input("Nhập tên file mới: "))
    filen=open(file_new, "w")
    filen.write(noidung)
    filen.close()
def cau5():
    file_goc = str(input("Nhập tên file gốc: "))
    file_dich = str(input("Nhập vị trí file mới: "))
    shutil.move(file_goc, file_dich)
    print("Đã di chuyển file thành công\n")

def cau6():
    file_remove = str(input("Nhập vị trí file muốn remove : "))
    os.remove(file_remove)
    print("Đã xóa file thành công\n")

def cau7():
    file = open("bangcuuchuong.txt", "r")
    noidung = file.read()
    file.close()
    if "5*5=25" in noidung:
        print("Có bảng cửu chương 5")
    else:
        print("Không có bảng cửu chương 5")
    
def cau8():
    file_name = str(input("Nhập tên file muốn đổi: "))
    new_name = str(input("Nhập tên mới: "))
    os.rename(file_name, new_name)
    print("Đã đổi tên file thành công\n")

def cau9():
    file_name = str(input("Nhập tên file muốn kiểm tra: "))
    if os.path.exists(file_name):
        print("File tồn tại")
    else:
        print("File không tồn tại")
def cau10():

    file_name = str(input("Nhập tên file muốn tạo: "))
    file=open(file_name, "w")
    list = random.sample(range(1,10000), 100)
    file.write("".join(map(str,list)))
    file.close()
    max=list.sort[-1]
    min=list.sort[0]
    tbc= (min+max)/2
    filer.close()
    file=open(file_name, "a")
    file.write("\n" + str(max) + "\n" + str(min) + "\n" + str(tbc))
    file.close()
    filer=open(file_name, "r")
    print(filer.read())
    file.close()
    print("Đã thêm vào file thành công\n")

def cau11():
    file_name = str(input("Nhập tên file muốn tạo: "))
    file=open(file_name, "w")
    du_lieu = [
    ['Tên', 'Tuổi'],
    ['John', 25],
    ['Alice', 30]
]
    for i in du_lieu:
        file.write(str(i) + "\n")
    file.close()
    file=open(file_name, "r")
    print(file.read())
    file.close()

def cau12():
    file_name= input("Nhập tên file muốn tạo: ")

    file = open(file_name, "w")
    file.close()
    file = open(file_name, "a")
    ten = input("Nhập tên: ")
    file.write("Tên: "+ten + "\n")
    tuoi = input("Nhập tuổi: ")
    file.write("tuổi: "+tuoi + "\n")
    quequan = input("Nhập quê quán: ")
    file.write("Quê quán:"+ quequan + "\n")
    tinhtranghonnhan = input("Nhập tình trạng hôn nhân: ")
    file.write("tình trạng hôn nhân:" +tinhtranghonnhan + "\n")
    email=input("Email: ")
    file.write("Email: " + email + "\n")
    file.close()

    file=open(file_name,"r")
    email=file.read()
    if "gmail.com" in email:
        print("Email tồn tại")
    else:
        print("Người dùng ko nhập email")
    file.close()
def cau13():
    # file_name = str(input("Nhập tên file muốn tạo: "))
    # file=open(file_name, "w")
    # tiennha= int(input("nhap vao so tien nha: "))
    # tienphong= int(input("nhap vao so tien phong: "))
    # tiendien = int(input("nhap vao so tien dien: "))
    # tiennuoc = int(input("nhap vao so tien nuoc: "))
    # tienguixe = int(input("nhap vao so tien gui xe: "))

    # file.write("tiền nhà: " + str(tiennha) +"\n")
    # file.write("tiền phòng: " + str(tienphong) +"\n")
    # file.write("tiền điện: " + str(tiendien) +"\n")
    # file.write("tiền nước: " + str(tiennuoc) +"\n")
    # file.write("tiền gửi xe: " + str(tienguixe) +"\n")

    # file.close()
    
    with open("sinhhoat.txt", "r") as filer:
        timkiem = input("Nhập vào nội dung muốn tìm kiếm: ")
        noidung = filer.read()
        if timkiem in noidung:
            for dong in noidung.split('\n'):
                if timkiem in dong:
                    print(dong.strip())
        else:
            print("Không tìm thấy thông tin.")

def cau14():
    file_name = str(input("Nhập tên file muốn xoa : "))
    file=open(file_name, "r")
    text= file.read()
    canxoa= input("nhap vao noi dung muon xoa: ")
    if canxoa in text:
        text=text.replace(canxoa, "")
        file.close()
        file=open(file_name, "w")
        file.write(text)
        file.close()
        print("Đã xóa thông tin thành công\n")
    file.close()



while True:
    print("1. Tạo tệp tin số ngẫu nhiên, có phần mở rộng là txt và đọc nội dung của nó.")
    print("2. Tạo một tệp tin văn bản mới có phần mở rộng là h5, đọc và ghi dữ liệu vào nó.")
    print("3. Thêm nhập và thêm bảng cửu chương vào tệp tin mới với tên file là bangCuuChuong.txt.")
    print("4. Sao chép nội dung của một tệp tin văn bản câu 3 sang một tệp tin khác bất kỳ.")
    print("5. Di chuyển một tệp tin từ thư mục này sang thư mục khác.")
    print("6. Xóa một tệp tin khỏi một thư mục di chuyển ở câu 5.")
    print("7. Kiểm tra thông tin tệp tin ở câu 3 và cho biết có bảng cửu chương 5 không?")
    print("8. Đổi tên một tệp tin câu 1 thành tên yêu thích của em.")
    print("9. Kiểm tra xem một tệp tin có tồn tại hay không.")
    print("10. Hãy nhập tự động 100 số vào file và tìm xem số lớn nhất và nhỏ nhất và từ đó tính trung bình giữa chúng.")
    print("11. Đọc và ghi dữ liệu vào một tệp tin CSV với thông tin là hai cột và 2 dòng.")
    print("12. Nhập thông tin vào file và kiểm tra có tồn tại thông tin nào là email không? (Email có phần mở rộng là gmail.com).")
    print("13. Đưa toàn bộ thông tin về chi tiêu hàng tháng của em vào file, hãy đọc thông tin theo yêu cầu từ bàn phím.")
    print("14. Xóa thông tin từ câu 13 theo yêu cầu.")
    chon=int(input("nhap vao lua chon: "))
    match(chon):
        case 1:
            cau1()
        case 2:
            cau2()
        case 3:
            cau3()
        case 4:
            cau4()
        case 5:
            cau5()
        case 6:
            cau6()
        case 7:
            cau7()
        case 8:
            cau8()
        case 9:
            cau9()
        case 10:
            cau10()
        case 11:
            cau11()
        case 12:
            cau12()
        case 13:
            cau13()
        case 14:
            cau14()