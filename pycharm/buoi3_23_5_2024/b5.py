print("b5: tim so lon nhat")

x = int(input("nhap vao so nguyen x: "))


y = int(input("nhap vao so nguyen y: "))

z = int(input("nhap vao so nguyen z: "))

if x > y and x > z:
    print("so lon nhat la: ", x)
elif y > z and y >x:
    print("so lon nhat la: ", y)
else:
    print("so lon nhat la: ", z)
    