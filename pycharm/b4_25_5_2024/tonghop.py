
import math


def main():
    
    print(
        "1.    Tính tổng số tiền của 250 000 con Gà cần mua vào mỗi mùa với số Gà được nhập từ SG (giá 15 nghìn/con):")
    print("      Biết:")
    print("      + Mua vào mùa Xuân: giá tăng 15%")
    print("      + Mua vào mùa Hè: giá giảm 10%")
    print("      + Mua vào mùa Thu: giá tăng 25%")
    print("      + Mua vào mùa Đông: giá giảm 40%")
    print("      Từ đó hãy cho biết nên mua gà vào mùa nào là hợp lý?\n")

    print("2.    Tính Tổng và Hiệu của các số chẵn và số lẻ được nhập từ bàn phím với 10 số.\n")

    print("3.    Tính số lượng gà và chuột biết có tổng 50 con và 100 chân.\n")

    print("4.    Tính số lượng Chó và Gà biết có Hiệu giữa chúng là 72 con và có 100 chân với Số Gà nhiều hơn Chó.\n")

    print("5.    Chuyển đổi nhiệt độ từ độ C sang độ F và ngược lại.\n")

    print("6.    Kiểm tra xem một năm sinh của bạn có phải là năm nhuận hay không và cho biết tuổi của bạn.\n")

    print("7.    Tìm ước số chung lớn nhất và bội số chung nhỏ nhất của 2 số.\n")

    print("8.    Chuyển đổi giữa hệ thập phân sang nhị phân, và ngược lại.\n")

    print("9.    Viết chương trình tìm giao điểm của 2 đường thẳng.\n")

    print("10.    Tìm số xuất hiện nhiều và ít nhất trong một danh sách.\n")

    print("11.    Tìm số lớn thứ 2 và nhỏ thứ 2 trong một danh sách.\n")

    print("12.    Tính toán diện tích và chu vi các hình học khác như hình thang, hình bình hành.\n")

    print("13.    Viết chương trình tính tổng, tích, trung bình của các số trong một danh sách.\n")

    print("14.    Viết chương trình đọc số, ví dụ nhập 1 hiển thị là Một (sử dụng switch).\n")

    print("15.    Viết chương trình để giải phương trình bậc nhất.\n")

    print("16.    Viết chương trình để giải phương trình bậc 2.\n")

    print("17.    Viết chương trình để kiểm tra xem chuỗi có phải là chuỗi liên tiếp âm dương hay không. \n")

    print("18.    Viết chương trình Python dùng map() và filter() để tạo list chứa giá trị bình phương của các số chẵn trong. \n")

    print("19.    Viết một chương trình tính 1/2 + 2/3 + 3/4 + ... + n/(n + 1) với một n là số được nhập vào (n> 0).\n")

    print("20.    Viết chương trình tính tổng các số chẵn trong dãy số.\n")

    print("21.   Viết chương trình tạo ngẫu nhiên list gồm 5 số chẵn nằm trong đoạn mà người dùng nhập. \n")

    print("0.    thoát \n")

    while True:
        i = int(input("nhập vào bài toán muốn giải trong các bài sau: "))
        if i == 1:
            bai1()
        elif i == 2:
            bai2()
        elif i == 3:
            bai3()
        elif i == 4:
            bai4()
        elif i == 5:
            bai5()
        elif i == 6:
            bai6()
        elif i == 7:
            bai7()
        elif i == 8:
            bai8()
        elif i == 9:
            bai9()
        elif i == 10:
            bai10()
        elif i == 11:
            bai11()
        elif i == 12:
            bai12()
        elif i == 13:
            bai13()
        elif i == 14:
            bai14()
        elif i == 15:
            bai15()
        elif i == 16:
            bai16()
        elif i == 17:
            bai17()
        elif i == 18:
            bai18()
        elif i == 19:
            bai19()
        elif i == 20:
            bai20()
        elif i == 21:
            bai21()
        elif i == 0:
            break
            


def bai1():
    print("1: Mua vào mùa Xuân: giá tăng 15%")
    print("2: Mua vào mùa Hè: giá giảm 10%")
    print("3: Mua vào mùa Thu: giá tăng 25%")
    print("4: Mua vào mùa Đông: giá giảm 40%")
    print("5: thoat ")
    i = int(input("nhap vao mua ma ban mua: "))

    while True:
        if i == 1 :
            print("gia tien mua 250000 con ga la: ",250000*(15000+(15/100*1500)))
            break
        elif i == 2 :
            print("gia tien mua 250000 con ga la: ",250000*(15000-(10/100*1500)))
            break
        elif i == 3 :
            print("gia tien mua 250000 con ga la: ",250000*(15000+(25/100*1500)))
            break
        elif i == 4 :
            print("gia tien mua 250000 con ga la: ",250000*(15000-(40/100*1500)))
            break
        elif i == 5 :
            break


    
def bai2():
    li = list(input("Nhập vào 10 số (nhập 'x' để thoát): ").split())
    print("x để thoát:")
    
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
    print("Tổng các số chẵn:", sumc)
    print("Tổng các số lẻ:", suml)



def bai3():
    for ga in range(51):
        for chuot in range(51):
            if (chuot + ga) == 50 and ((chuot * 4) + (ga * 2)) == 100:
                print("So chuot la: ", chuot, "; So ga la: ", ga)


def bai4():
    for ga in range(73):
        for cho in range(51):
            if (ga- cho ) == 72 and ((cho * 4) + (ga * 2)) == 100:
                print("So cho la: ", cho, "; So ga la: ", ga)
                break
    else:
        print("khong ton tai so ga va cho hop le")
    

def bai5():
    
    while True:
        print("1: doi do c")
        print("2: doi do f")
        print("3: thoat")
        i=int(input("nhập lựa chọn: "))
        if i== 1 :
            c= float(input("Nhập vào độ c: "))
            print("Do F la: ",c*1.8+32)
       
        elif i== 2 :
            f= float(input("Nhập vào độ f: "))
            print("Do C la: ",(f-32)/1.8)
          
        elif i== 3 :
            break
        else:
            print("nhập lại lựa chọn")
            i=int(input("nhập lựa chọn: "))
    

def bai6():
    namsinh= int(input("nhap vao nam sinh cua ban: "))

    if namsinh % 400 ==0:
        print(namsinh,"la nam nhuan")
        print("tuoi cua ban la: ",2024-namsinh)
    elif namsinh % 4 ==0 & namsinh % 100 !=0:
        print(namsinh,"la nam nhuan")
        print("tuoi cua ban la: ",2024-namsinh)
    else:
        print(namsinh,"khong la nam nhuan")
        print("tuoi cua ban la: ",2024-namsinh)

def bai7():
    
    a= int(input("nhap vao a: "))
    b= int(input("nhap vao b: "))
    
    c=a*b

    while a != b:
        if a > b:
            a -= b
        else:
            b = b - a
   
    print("UCLN= ",a)
    print("BCNN= ",c//a)

def bai8():
    while True:
        print("1: thap phan sang nhi phan")
        print("2: nhi phan sang thap phan")
        print("3: thoat")
        i=int(input("nhập lựa chọn: "))
        if i== 1 :
            n= int(input("nhap vao so thap phan: "))
            print("so nhi phan la: ",bin(n))
       
        elif i== 2 :
            n= input("nhap vao so nhi phan: ")
            print("so thap phan la: ",int(n,2))
          
        elif i== 3 :
            break
        else:
            print("nhập lại lựa chọn")
            i=int(input("nhập lựa chọn: "))

def bai9():
    print("Nhập vào các hệ số của phương trình đường thẳng thứ nhất (ax + by + c = 0):")
    a1 = float(input("Nhập hệ số a1: "))
    b1 = float(input("Nhập hệ số b1: "))
    c1 = float(input("Nhập hệ số c1: "))

    print("Nhập vào các hệ số của phương trình đường thẳng thứ hai (ax + by + c = 0):")
    a2 = float(input("Nhập hệ số a2: "))
    b2 = float(input("Nhập hệ số b2: "))
    c2 = float(input("Nhập hệ số c2: "))

    # Tính determinant
    det = a1 * b2 - a2 * b1

    
    if det == 0:
        print("Hai đường thẳng là song song, không có giao điểm.")
    elif a1 ==a2 and b2 == b1 and c1 == c2:
        print("Hai đường thẳng trùng nhau.")
    else:
        
        x = (b2 * c1 - b1 * c2) / det
        y = (a1 * c2 - a2 * c1) / det
        print("Toạ độ giao điểm là: (", x, ",", y, ")")   

def bai10():
    li= list(input("nhap vao 10 so: ").split())
    dic = {}
    for i in li:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(dic)
    print("so xuat hien nhieu nhat la: ",max(dic,key=dic.get))
    print("so xuat hien it nhat la: ",min(dic,key=dic.get))

def bai11():
    li = list(input("nhap vao 10 so: ").split())
    li.sort()

    print("so lon thu 2 la: ",li[-2])
    print("so nho thu 2 la: ",li[1])
def bai12():   
    #Tính toán diện tích và chu vi các hình học khác như hình thang, hình bình hành.
    while True:
        print("1: dien tich va chu vi hinh chu nhat")
        print("2: dien tich va chu vi hinh tron")
        print("3: dien tich va chu vi hinh thang")
        print("4: dien tich va chu vi hinh binh hanh")
        print("5: thoat")
        i=int(input("nhập lựa chọn: "))
        if i== 1 :
            a= float(input("nhap vao chieu dai: "))
            b= float(input("nhap vao chieu rong: "))
            print("dien tich la: ",a*b)
            print("chu vi la: ",2*(a+b))
       
        elif i== 2 :
            r= float(input("nhap vao ban kinh: "))
            print("dien tich la: ",3.14*r*r)
            print("chu vi la: ",2*3.14*r)
          
        elif i== 3 :
            a= float(input("nhap vao day lon: "))
            b= float(input("nhap vao day be: "))
            h= float(input("nhap vao chieu cao: "))
            print("dien tich la: ",(a+b)*h/2)
            print("chu vi la: ",a+b+2*h)
        elif i== 4 :
            a= float(input("nhap vao chieu dai: "))
            b= float(input("nhap vao chieu rong: "))
            print("dien tich la: ",a*b)
            print("chu vi la: ",2*(a+b))
        elif i== 5 :
            break
        else:
            print("nhập lại lựa chọn")
            i=int(input("nhập lựa chọn: "))
def bai13():
    li= list(input("nhap vao danh sach so: ").split())
    sum = 0
    tich = 1
    tb=0
    for i in li:
        i=int(i)
        sum += i
        tich *= i
    tb = sum/len(li)       
    print("tong la: ",sum)
    print("tich la: ",tich)
    print("trung binh la: ",tb)    

def bai14():
    so = int(input("Nhập vào số cần dịch (từ 1 đến 10): "))
    num = {
        1: "một",
        2: "hai",
        3: "ba",
        4: "bốn",
        5: "năm",
        6: "sáu",
        7: "bảy",
        8: "tám",
        9: "chín",
        10: "mười"
    }

    if so in num:
        print(f"Số {so} tương ứng với '{num[so]}'")
    else:
        print("Số không hợp lệ! Vui lòng nhập số từ 1 đến 10.")




def bai15():
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    if a == 0:
        if b == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -b / a
        print("Nghiệm của phương trình là: ", x)

def bai16():
    a= float(input("nhap vao a: "))
    b= float(input("nhap vao b: "))
    c= float(input("nhap vao c: "))
    denta = b*b - 4*a*c

    if denta < 0:
        print("phuong trinh vo nghiem")
    elif denta == 0:
        print("phuong trinh co nghiem kep: ",-b/(2*a))
    else:
        print("phuong trinh co 2 nghiem phan biet: ",(-b+math.sqrt(denta))/(2*a),(-b-math.sqrt(denta))/(2*a))

def bai17():
    li=list(map(int,input("Nhập vào 1 list: ").split()))
    for i in range(len(li)-1):
        if li[i]*li[i+1]<0:
            print("chuoi nhap vao lien tiep am duong")
            return
        print("chuoi nhap vao khong lien tiep am duong")

def bai18():
    print("Viết chương trình Python để tạo list chứa giá trị tổng bình phương của các số chẵn trong list")
    li = list(map(int,input("nhap vao chuoi : ").split()))
    chuoi= []
    sum = 0

    for i in li :
        if i%2 == 0 :
            chuoi.append(i*i)
            sum += i*i
    print(chuoi)
    print("tong la: ",sum)


def bai19():
    print("Viết một chương trình tính 1/2 + 2/3 + 3/4 + ... + n/(n + 1) với một n là số được nhập vào (n> 0).")
    n = int(input("nhap vao n: "))
    sum = 0
    for i in range(1,n+1):
        sum += i/(i+1)
    print("tổng của dãy là: ",sum)


def bai20():
    print("nhập vào phép tính để máy tính tính ra kết quả \n")
    x = input("nhap vap biểu thức bạn muốn tính : ")
    print(eval(x))

def bai21():
    print("Viết chương trình Python để tạo list chứa 5 số ngẫu nhiên từ 2 giới hạn mà người dùng nhập. \n")
    import random
    x = int(input("nhập vào giới hạn đầu trái: \n"))
    y = int(input("nhập vào giới hạn đầu phải: \n"))
    if x>y or x==y :
        print("x không được lớn hơn y")
    else:
        print(random.sample([i for i in range(x,y) if i % 2 == 0], 5))


if __name__ == '__main__':
    main()


        


    
