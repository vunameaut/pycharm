import random
def docfile():
    file_name=input("Nhập tên file: ")
    file=open(file_name, "r")
    print(file.read())
    file.close()
file_path = "D:\hoc tap\python\file_path"
def cau1():
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
    print(file.read())
    file.close()

def cau2():
    file_name=input("Nhập tên file: ")
    soluong = int(input("Nhập vào so luong bạn muốn thêm: "))
    for i in range(soluong):
        open(file_name,"a")
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
        file.close()
    
    


def cau3():
    file = open("tinhtoan.txt", "a")
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    tich = a * b
    tong = a + b
    hieu = a - b
    thuong = a / b
    file.write("a: " + str(a) + "\n")
    file.write("b: " + str(b) + "\n")
    file.write("Tổng: " + str(tong) + "\n")
    file.write("Hiệu: " + str(hieu) + "\n")
    file.write("Tích: " + str(tich) + "\n")
    file.write("Thương: " + str(thuong) + "\n")
    file.close()
    
   
def cau4():
    file = open("matcuoi.txt", "w")
    file.write("   *****   \n")
    file.write(" *       * \n")
    file.write("*   O   O  *\n")
    file.write("*     <    *\n")
    file.write(" *  \\__/  *\n")
    file.write("   *****  \n")
    file.close()
    file = open("matcuoi.txt", "r")
    print(file.read())
    file.close()

def cau5():
    li = list(input("Nhập vào 10 số : ").split())
    file = open("dayso.txt", "w")
    file.write(" ".join(li))

    sumc = 0
    suml = 0
    for i in li:
        if i == "x":
            break
        i = int(i)
        if i % 2 == 0:
            sumc += i
        else:
            suml += i
    file.write("\nTổng số chẵn: " + str(sumc) + "\n")
    file.write("Tổng số lẻ: " + str(suml) + "\n")

def cau6():
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
    file.write("Số ký tự: " + str(len(ten) + len(tuoi) + len(quequan) + len(tinhtranghonnhan)) + "\n")
    file.close()

def cau7():
    n = int(input("nhap vao n: "))
    giaithua = 1
    for i in range(1,n+1):
        giaithua *= i
    print("giai thua cua ",n," la: ",giaithua)
    file = open("giaithua.txt", "w")
    file.write("Giai thừa của " + str(n) + " là: " + str(giaithua))
    file.close()
def cau8():
    tongdiem = 0
    diemtb = 0
    for i in range(5):
        file = open("diem.txt", "a")
        ten = input("Nhập tên sinh viên: ")
        file.write("Tên sinh viên: " + ten + "\n")
        
        for j in range(5):
            diem = float(input("Nhập điểm môn học: "))
            file.write("Điểm môn học " + str(j+1) + ": " + str(diem) + "\n")
            tongdiem += diem
        diemtb = tongdiem / 5
        file.write("Tổng điểm: " + str(tongdiem) + "\n")
        file.write("Điểm trung bình: " + str(diemtb) + "\n")
        file.close()
def cau9():
    li = list(input("Nhập vào danh sách thư mời: ").split())
    file = open("thumoi.txt", "w")
    file.write(" ".join(li))
    file.close()
    file = open("thumoi.txt", "r")
    tencanxoa= input("Nhập tên cần xóa: ")
    new_list= [li for li in li if li != tencanxoa]
    file = open("thumoi.txt", "w")
    file.write(" ".join(new_list))
    file.close()
def cau10():

    numbers = random.sample(range(1, 1001), 10)
    file = open("danhsach.txt", "w")
    file.write(" ".join(map(str, numbers)))
    numbers.sort()
    solonnhat = numbers[-1]
    sonhonhat = numbers[0]
    print(numbers)
    file.write("\nSố lớn nhất: " + str(solonnhat) + "\n")
    file.write("Số nhỏ nhất: " + str(sonhonhat) + "\n")
    file.close()
def cau11():
    sumc = 0
    n = int(input("Nhập vào số tự nhiên n: "))  
    for i in range(1, n + 1):
        if i % 2 == 0:
            sumc += i

    with open("dayso.txt", "w") as file:
        file.write(str(n) + "!")
        file.write("\nTổng số chẵn: " + str(sumc) + "\n")
    


while True:
    
    print("0: để đọc file")
    print("1: Em hãy tạo một file là tên của em, trong file có đầy đủ thông tin cá nhân. (Thông tin nhập từ bàn phím)")
    print("2: Từ câu 1, em hãy thêm thông tin của bạn em và đọc toàn bộ thông tin có trong file.")
    print("3: Nhập thông tin hai số a và b vào file, tính tổng, hiệu, tích và thương của hai số đấy.")
    print("4: Vẽ một hình mặt cười vào file và đọc mặt cười đấy.")
    print("5: Nhập vào 1 dãy số tự động vào file, tính tổng và tích các số lẻ và số chẵn từ file đó.")
    print("6: Nhập đầy đủ thông tin cá nhân của em và đếm ký tự của file đấy.")
    print("7: Nhập vào số tự nhiên n vào file, tính giai thừa của số đấy.")
    print("8: Nhập vào điểm của 5 sinh viên với 5 môn học khác nhau, Tính tổng và trung bình của mỗi em. Tìm ra sinh viên có điểm trung bình cao nhất và thấp nhất.")
    print("9: Tạo một danh sách thư mời đến bữa tiệc sinh nhật, hãy xóa một thành viên có trong thư mời đó bất kỳ.")
    print("10: Tạo một danh sách các số tự nhiên từ 1 đến 100, tìm ra số lớn nhất và nhỏ nhất.")
    print("11:  Nhập vào sô tự nhiên n vào file, tính tong của các số chẵn từ 1 đến n.")
    print("12: Thoát")
    chon=int(input("nhap vao lua chon: "))

    match(chon):
        case 0:
            docfile()
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
            break

        
        
           

