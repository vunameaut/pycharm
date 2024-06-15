import math
#hình tròn
print("---------------------tính hình tròn ---------------------------")
bankinh=float(input("nhap ban kinh hinh tron: "))


dientichhinhtron = 2* math.pi * bankinh
chuvihinhtron = math.pi * bankinh **2

print("dien tich hinh tron la: ",dientichhinhtron)
print("chu vi hinh tron la: ",chuvihinhtron)

print("--------------------tính hình tam giác ----------------------------")
#hinh tam giác
canh1=float(input("nhap vao canh 1: "))
canh2=float(input("nhap vao canh 2: "))
canh3=float(input("nhap vao canh 3: "))

if canh1+canh2>canh3 and canh1 + canh3 > canh2 and canh3 + canh2 > canh1:
    chuvihinhtamgiac = canh1 + canh2 + canh3
    print("chu vi hinh tam giac la: ",chuvihinhtamgiac)
    dientichhinhtamgiac = math.sqrt(chuvihinhtamgiac*(chuvihinhtamgiac-canh1)*(chuvihinhtamgiac-canh2)*(chuvihinhtamgiac-canh3))
    print(" dientichhinhtamgiac: ",dientichhinhtamgiac)

else:
    print("khong phai la hinh tam giac")



