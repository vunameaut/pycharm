print("b17: Tạo một chương trình hỏi người dùng một con số và in ra tất cả ước số của con số đó.")

num = int(input("Nhập một số: "))

print("Các ước số của", num, "là:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)


