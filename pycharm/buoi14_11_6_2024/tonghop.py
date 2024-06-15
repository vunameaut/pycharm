import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import font
from PIL import ImageTk


def cau6():
    with sqlite3.connect("it9.db") as conn:
        cursor = conn.cursor()
    ten = str(input("Nhập vào ten tac gia: "))
    cursor.execute("""SELECT Books.title,Books.datePub, Authors.Name
    FROM Authors

    INNER JOIN Books ON Authors.Name = Books.Author
    WHERE Authors.Name = ?
    ORDER BY Books.datePub;""", (ten,))

    result = cursor.fetchall()
    for row in result:
        print(' - '.join(map(str, row)))


def cau7():
    with sqlite3.connect("TestScores.db") as conn:
        cursor = conn.cursor()
    cursor.execute(("""create table if not exists b1 (
    ten text PRIMARY KEY ,
    gioitinh text NOT NULL );"""))

    w = tk.Tk()
    w.title("Thông tin người dùng")
    # Labels
    ten_label = tk.Label(w, text="Nhập vào tên :")
    ten_label.grid(row=0, column=0)
    gioitinh_label = tk.Label(w, text="Nhập vào giới tính :")
    gioitinh_label.grid(row=1, column=0)
    # Entry fields
    entry_ten = tk.Entry(w)
    entry_ten.grid(row=0, column=1)
    entry_gioitinh = tk.Entry(w)
    entry_gioitinh.grid(row=1, column=1)
    # Button functions


def add():
    ten = entry_ten.get()
    gioitinh = entry_gioitinh.get()
    cursor.execute("""INSERT INTO b1 (ten, gioitinh) VALUES (?,?)""",
                   (ten, gioitinh))
    conn.commit()
    print(("them thanh cong"))


def clear():
    entry_ten.delete(0, END)
    entry_gioitinh.delete(0, END)


def exit_program():
    w.destroy()
    # Buttons
    btnadd = tk.Button(w, text="Thêm", command=add)
    btnadd.grid(row=2, column=0)
    btnclear = tk.Button(w, text="Xóa", command=clear)
    btnclear.grid(row=2, column=1)
    btnexit = tk.Button(w, text="Thoát", command=exit_program)
    btnexit.grid(row=2, column=2)
    w.mainloop()


def cau8():
    w = tk.Tk()

    def list():
        ten = nguon_nhap.get()

    if ten.isdigit():
        nhom_ketqua.insert(END, ten)
        nguon_nhap.delete(0, END)
    else:
        nguon_nhap.delete(0, END)


def xoa():
    nhom_ketqua.delete(0, END)
    nhan_dan = Label(text="Nhập số vào đây:")
    nhan_dan.pack(pady=10)
    nguon_nhap = Entry()
    nguon_nhap.pack(pady=5)
    them = Button(text="Thêm vào danh sách ", command=list)
    them.pack(pady=5)
    xoa = Button(text="Xóa danh sách ", command=xoa)
    xoa.pack(pady=5)
    nhom_ketqua = Listbox()
    nhom_ketqua.pack(pady=6)
    w.mainloop()


def cau9():
    w = Tk()

    def list():
        ten = nguon_nhap.get()

    if ten.isdigit():
        nhom_ketqua.insert(END, ten)
        nguon_nhap.delete(0, END)
    else:
        nguon_nhap.delete(0, END)

    def luu():
        noidung = nhom_ketqua.get(0, END)

    with open("dulieu.csv", "w") as file:
        for i in noidung:
            file.write(i + "\n")
    with open("dulieu.csv", "r") as filer:
        print(filer.read())
    nhan_dan = Label(text="Nhập số vào đây:")
    nhan_dan.pack(pady=10)
    nguon_nhap = Entry()
    nguon_nhap.pack(pady=5)
    them = Button(text="Thêm vào danh sách ", command=list)
    them.pack(pady=5)
    luu_file = Button(text="luu thanh file dạng csv ", command=luu)
    luu_file.pack(pady=5)
    nhom_ketqua = Listbox()
    nhom_ketqua.pack(pady=6)
    w.mainloop()


def cau10():
    w = Tk()


w.geometry("500x500")
font_large = font.Font(family="Helvetica", size=20, weight="bold")
tiltle = Label(w, text="Welcome to my program", font=font_large)
tiltle.grid(row=0, column=2)
btnview = Button(text="View", font=font_large)
btnview.grid(row=3, column=0)
btnadd = Button(text="Add", font=font_large)
btnadd.grid(row=3, column=3)
btndelete = Button(text="Delete", font=font_large)
btndelete.grid(row=6, column=0)
btnupdate = Button(text="Update", font=font_large)
btnupdate.grid(row=6, column=3)
btnexit = Button(text="Exit", font=font_large)
btnexit.grid(row=9, column=2)
w.mainloop()


def cau11():
    w = tk.Tk()


w.geometry("300x300")

w.title("Đăng nhập")
with sqlite3.connect("TestScores.db") as conn:
    cursor = conn.cursor()
# Labels
username_label = tk.Label(w, text="Username:")
username_label.grid(row=0, column=0)
password_label = tk.Label(w, text="Password:")
password_label.grid(row=1, column=0)
# Entry fields
entry_username = tk.Entry(w)
entry_username.grid(row=0, column=1)
entry_password = tk.Entry(w, show="*")
entry_password.grid(row=1, column=1)


# Button functions
def login():
    username = entry_username.get()


password = entry_password.get()
cursor.execute("SELECT * FROM login WHERE user = ? AND pass = ?",
               (username, password))
rows = cursor.fetchall()
if len(rows) > 0:
    print("Đăng nhập thành công")
else:
    print("Đăng nhập thất bại")


def exit_program():
    w.destroy()


# Buttons
btn_login = tk.Button(w, text="Login", command=login)
btn_login.grid(row=2, column=0)
btn_exit = tk.Button(w, text="Exit", command=exit_program)
btn_exit.grid(row=2, column=2)
w.mainloop()


def cau12():
    w = tk.Tk()


w.geometry("400x400")
w.title("Đăng ký")
with sqlite3.connect("TestScores.db") as conn:
    cursor = conn.cursor()
# Labels
ho_ten_label = tk.Label(w, text="Họ tên:")
ho_ten_label.grid(row=0, column=0)
tuoi_label = tk.Label(w, text="Tuổi:")
tuoi_label.grid(row=1, column=0)
lop_label = tk.Label(w, text="Lớp:")
lop_label.grid(row=2, column=0)
ma_sv_label = tk.Label(w, text="Mã sinh viên:")
ma_sv_label.grid(row=3, column=0)
nam_hoc_label = tk.Label(w, text="Năm học:")

nam_hoc_label.grid(row=4, column=0)
thanh_tich_label = tk.Label(w, text="Thành tích:")
thanh_tich_label.grid(row=5, column=0)
so_thich_label = tk.Label(w, text="Sở thích:")
so_thich_label.grid(row=6, column=0)
ghi_chu_label = tk.Label(w, text="Ghi chú:")
ghi_chu_label.grid(row=7, column=0)
# Entry fields
entry_ho_ten = tk.Entry(w)
entry_ho_ten.grid(row=0, column=1)
entry_tuoi = tk.Entry(w)
entry_tuoi.grid(row=1, column=1)
entry_lop = tk.Entry(w)
entry_lop.grid(row=2, column=1)
entry_ma_sv = tk.Entry(w)
entry_ma_sv.grid(row=3, column=1)
entry_nam_hoc = tk.Entry(w)
entry_nam_hoc.grid(row=4, column=1)
entry_thanh_tich = tk.Entry(w)
entry_thanh_tich.grid(row=5, column=1)
entry_so_thich = tk.Entry(w)
entry_so_thich.grid(row=6, column=1)
entry_ghi_chu = tk.Entry(w)
entry_ghi_chu.grid(row=7, column=1)


# Button function
def save():
    ho_ten = entry_ho_ten.get()


tuoi = entry_tuoi.get()
lop = entry_lop.get()
ma_sv = entry_ma_sv.get()
nam_hoc = entry_nam_hoc.get()
thanh_tich = entry_thanh_tich.get()
so_thich = entry_so_thich.get()
ghi_chu = entry_ghi_chu.get()
cursor.execute("CREATE TABLE IF NOT EXISTS students (ho_ten TEXT,
tuoi
INTEGER, lop
TEXT, ma_sv
TEXT, nam_hoc
TEXT, thanh_tich
TEXT,
so_thich
TEXT, ghi_chu
TEXT)")
cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?,
?)", (ho_ten, tuoi, lop, ma_sv, nam_hoc, thanh_tich, so_thich, ghi_chu))
conn.commit()
print("Đăng ký thành công")


def clear():
    entry_ho_ten.delete(0, tk.END)


entry_tuoi.delete(0, tk.END)
entry_lop.delete(0, tk.END)
entry_ma_sv.delete(0, tk.END)
entry_nam_hoc.delete(0, tk.END)
entry_thanh_tich.delete(0, tk.END)
entry_so_thich.delete(0, tk.END)
entry_ghi_chu.delete(0, tk.END)


def edit():
    ho_ten = entry_ho_ten.get()


tuoi = entry_tuoi.get()
lop = entry_lop.get()
ma_sv = entry_ma_sv.get()

nam_hoc = entry_nam_hoc.get()
thanh_tich = entry_thanh_tich.get()
so_thich = entry_so_thich.get()
ghi_chu = entry_ghi_chu.get()
cursor.execute('''UPDATE students
SET ho_ten = ?, tuoi = ?, lop = ?, nam_hoc = ?,
thanh_tich = ?, so_thich = ?, ghi_chu = ?
WHERE ma_sv = ?'''
               , (ho_ten, tuoi, lop, ma_sv, nam_hoc, thanh_tich,
                  so_thich, ghi_chu))
conn.commit()
print("Sửa thành công")


def delete():
    ho_ten = entry_ho_ten.get()


tuoi = entry_tuoi.get()
lop = entry_lop.get()
ma_sv = entry_ma_sv.get()
nam_hoc = entry_nam_hoc.get()
thanh_tich = entry_thanh_tich.get()
so_thich = entry_so_thich.get()
ghi_chu = entry_ghi_chu.get()
cursor.execute('''DELETE students
SET ho_ten = ?, tuoi = ?, lop = ?, nam_hoc = ?,
thanh_tich = ?, so_thich = ?, ghi_chu = ?
WHERE ma_sv = ?'''
               , (ho_ten, tuoi, lop, ma_sv, nam_hoc, thanh_tich,
                  so_thich, ghi_chu))
conn.commit()
print("Xóa thành công")


def exit_program():
    w.destroy()


# Buttons
btn_save = tk.Button(w, text="Lưu", command=save)
btn_save.grid(row=8, column=0)
btn_save = tk.Button(w, text="sửa", command=edit)
btn_save.grid(row=8, column=3)
btn_clear = tk.Button(w, text="clear", command=clear)
btn_clear.grid(row=8, column=1)
btn_clear = tk.Button(w, text="xóa", command=delete)
btn_clear.grid(row=8, column=4)
btn_exit = tk.Button(w, text="Thoát", command=exit_program)
btn_exit.grid(row=8, column=2)
w.mainloop()
