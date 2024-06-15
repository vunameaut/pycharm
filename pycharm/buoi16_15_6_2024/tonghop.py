import mysql.connector

def taodatabse():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE sinhvien")

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sinhvien")
mycursor = mydb.cursor()
def taotable():
    
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            major VARCHAR(255),
            point FLOAT,
            note VARCHAR(255)
        )
    """)
    mydb.commit()
def them5sv():
    sql = "INSERT INTO students (name, age, major, point, note) VALUES (%s, %s, %s, %s, %s)"
    values = [
        ("John Doe", 20, "Computer Science", 4.0, "co"),
        ("Jane Smith", 22, "Mathematics", 3.5, "co"),
        ("Michael Johnson", 21, "Physics", 3.2, "khong"),
        ("Emily Davis", 19, "Chemistry", 3.8, "khong"),
        ("David Wilson", 23, "Biology", 3.0, "co")
    ]
    mycursor.executemany(sql, values)
    mydb.commit()
def them_moi_sinh_vien():
    name = input("Nhập tên của sinh viên: ")
    age = input("Nhập tuổi của sinh viên: ")
    major = input("Nhập ngành học của sinh viên: ")
    point = input("Nhập điểm của sinh viên: ")
    note = input("Nhập ghi chú của sinh viên: ")
    sql = "INSERT INTO students (name, age, major, point, note) VALUES (%s, %s, %s, %s, %s)"
    value = (name, age, major, point, note)
    mycursor.execute(sql, value)
    mydb.commit()

def cap_nhat_sinh_vien():
    id = input("Nhập ID của sinh viên cần cập nhật: ")
    name = input("Nhập tên mới của sinh viên: ")
    age = input("Nhập tuổi mới của sinh viên: ")
    major = input("Nhập ngành học mới của sinh viên: ")
    point = input("Nhập điểm mới của sinh viên: ")
    note = input("Nhập ghi chú mới của sinh viên: ")
    sql = "UPDATE students SET name = %s, age = %s, major = %s, point = %s, note = %s WHERE id = %s"
    value = (name, age, major, point, note, id)
    mycursor.execute(sql, value)
    mydb.commit()
def xoa_sinh_vien():
    id = input("Nhập ID của sinh viên cần xóa: ")
    sql = "DELETE FROM students WHERE id = %s"
    value = (id,)
    mycursor.execute(sql, value)
    mydb.commit()

def truy_van_tat_ca_sinh_vien():
    sql = "SELECT * FROM students"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for _ in result:
        print(_)
    mydb.commit()
def truy_van_sinh_vien_theo_ten_hoac_ma_lop():
    sql = "SELECT * FROM students WHERE name = %s OR major = %s"
    name = input("Nhập tên hoặc mã lớp của sinh viên: ")
    value = (name, name)
    mycursor.execute(sql, value)
    result = mycursor.fetchall()
    for _ in result:
        print(_)
    mydb.commit()
def sap_xep_sinh_vien_theo_ten():
    sql = "SELECT * FROM students ORDER BY name"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for _ in result:
        print(_)
    mydb.commit()
def tim_kiem_sinh_vien_cung_ten():
    sql = "SELECT * FROM students GROUP BY name"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for _ in result:
        print(_)
    mydb.commit()

def xoa_sinh_vien_co_note_la_co():
    sql = "DELETE FROM students WHERE note = %s"
    value = ("co",)
    mycursor.execute(sql, value)
    mydb.commit()
def hien_thi_sinh_vien_cung_tuoi():
    sql = "SELECT * FROM students GROUP BY age"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for _ in result:
        print(_)
    mydb.commit()

def tim_sinh_vien_co_diem_cao_nhat_va_thap_nhat():
    sql = "SELECT * FROM students ORDER BY point DESC LIMIT 1"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print("Sinh viên có điểm cao nhất:")
    for _ in result:
        print(_)
    sql = "SELECT * FROM students ORDER BY point ASC LIMIT 1"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print("Sinh viên có điểm thấp nhất:")
    for _ in result:
        print(_)
    mydb.commit()
def thay_diem_mot_sinh_vien_bat_ky():
    id = input("Nhập ID của sinh viên cần thay điểm: ")
    point = input("Nhập điểm mới của sinh viên: ")
    sql = "UPDATE students SET point = %s WHERE id = %s"
    value = (point, id)
    mycursor.execute(sql, value)
    mydb.commit()

def them_dong_tinh_tong_diem():
    sql = "SELECT SUM(point) FROM students"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    print("Tổng điểm của tất cả sinh viên:", result[0])
    mydb.commit()

while True:
        print("----- MENU -----")
        print("1. Thêm mới một sinh viên vào bảng")
        print("2. Cập nhật thông tin của một sinh viên dựa trên ID")
        print("3. Xóa một sinh viên dựa trên ID")
        print("4. Truy vấn tất cả sinh viên trong bảng")
        print("5. Truy vấn sinh viên theo tên hoặc mã lớp")
        print("6. Sắp xếp sinh viên theo tên")
        print("7. Tìm kiếm sinh viên có cùng tên")
        print("8. Xóa toàn bộ sinh viên có note là có")
        print("9. Hiển thị danh sách sinh viên có cùng tuổi")
        print("10. Tìm sinh viên có điểm (point) cao nhất và thấp nhất")
        print("11. Thay điểm một sinh viên bất kỳ")
        print("12. Thêm dòng dữ liệu cuối cùng để tính tổng điểm toàn bộ sinh viên")
        print("13. Thoát khỏi chương trình")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            them_moi_sinh_vien()
        elif choice == "2":
            cap_nhat_sinh_vien()
        elif choice == "3":
            xoa_sinh_vien()
        elif choice == "4":
            truy_van_tat_ca_sinh_vien()
        elif choice == "5":
            truy_van_sinh_vien_theo_ten_hoac_ma_lop()
        elif choice == "6":
            sap_xep_sinh_vien_theo_ten()
        elif choice == "7":
            tim_kiem_sinh_vien_cung_ten()
        elif choice == "8":
            xoa_sinh_vien_co_note_la_co()
        elif choice == "9":
            hien_thi_sinh_vien_cung_tuoi()
        elif choice == "10":
            tim_sinh_vien_co_diem_cao_nhat_va_thap_nhat()
        elif choice == "11":
            thay_diem_mot_sinh_vien_bat_ky()
        elif choice == "12":
            them_dong_tinh_tong_diem()
        elif choice == "13":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")



