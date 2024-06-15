print("b11: tinh giai thua cua n, với n nhap tu ban phim")

n = int(input("nhap vao n: "))

giaithua = 1

for i in range(1,n+1):
    giaithua = giaithua * i

print("giai thua cua ",n," la: ",giaithua)

