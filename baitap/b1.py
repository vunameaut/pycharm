# a +b =n
# a và b lẻ
# a >=b
# a-b min


n = int(input("Nhập vào 1 số: "))
for a in range(1,n):
    for b in range(a, n):

        if a + b == n and a % 2 != 0 and b % 2 != 0 :
            min = a - b
             
            break


