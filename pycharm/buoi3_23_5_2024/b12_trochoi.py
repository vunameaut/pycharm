print("b12: viết chương trình trò chơi đoán số vừa nhập, cho đoán tối đa 5 lần")

import random

x = random.randint(1, 100)

count = 0

while count < 5:
    sodoan = int(input("Nhập số bạn đoán: "))
    if sodoan == x:
        print("Chúc mừng bạn đã đoán đúng")
        break
    elif sodoan > x:
        print("Số bạn đoán lớn hơn số cần đoán")
    else:
        print("Số bạn đoán nhỏ hơn số cần đoán")
    count += 1

print("Số cần đoán là: ", x)