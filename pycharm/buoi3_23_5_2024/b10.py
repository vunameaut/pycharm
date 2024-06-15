print("b10: kiểm tra số nguyen tố")

x = int(input("nhap so nguyen: "))

if(x<2):
    print(x,"khong phai la so nguyen to")
else:
    for i in range(2,x):
        if(x%i==0):
            print(x,"khong phai la so nguyen to")
            break
    else:
        print(x,"la so nguyen to")