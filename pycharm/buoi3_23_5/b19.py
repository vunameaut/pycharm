print("b19: Tính tổng các số chẵn trong dãy số")

n = input("Nhập số một dãy số: ").split()
sum = 0
for i in n:
    i=int(i)
    if i % 2 == 0:
        sum += i

print("Tổng các số chẵn trong dãy số là:", sum)