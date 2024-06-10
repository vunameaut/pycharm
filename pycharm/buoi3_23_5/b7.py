print("b7: tìm ra bạn có điểm thấp nhất")

ban1 =float(input("Nhập điểm bạn 1: "))

ban2 =float(input("Nhập điểm bạn 2: "))

ban3 =float(input("Nhập điểm bạn 3: "))

ban4 =float(input("Nhập điểm bạn 4: "))

ban5 =float(input("Nhập điểm bạn 5: "))

diem = {
    "ban1": ban1,
    "ban2": ban2,
    "ban3": ban3,
    "ban4": ban4,
    "ban5": ban5,
}

diem_max =max(diem.values())
diem_min =min(diem.values())


ban_max = [ban for ban, diem in diem.items() if diem == diem_max]
ban_min = [ ban for ban, 
           
           
           
           diem in diem.items() if diem == diem_min]


print("Danh sách điểm: "),list(diem.values())

print("Bạn có điểm thấp nhất là: "),ban_min

print("Bạn có điểm cao nhất là: "),ban_max
