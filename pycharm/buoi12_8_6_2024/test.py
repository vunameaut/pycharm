import subprocess
from tkinter import *
import sqlite3

path = "D:/hoc tap/python/data/qlgv.db"
con = sqlite3.connect(path)




w = Tk()
w.geometry("400x400")





def check():
    tk = txt_tk.get()
    mk = txt_mk.get()
    cursor = con.cursor()
    sql = "select * from Dang_nhap where Ten_dang_nhap = ? and Mat_khau = ?"
    cursor.execute(sql,(tk,mk))
    result = cursor.fetchall()
    con.close()

    if result:
        print("Đăng nhập thành công")
        subprocess.Popen(["python", "D:/hoc tap/python/pycharm/buoi11_6_6_2024/toghop.py"])
    else:
        print("Đăng nhập thất bại")

taikhoan = Label(w, text="Tài khoản")
taikhoan.grid(row=0, column=0)

txt_tk = Entry()
txt_tk.grid(row=0, column=1)

matkhau = Label(w, text="Mật khẩu")
matkhau.grid(row=1, column=0)

txt_mk = Entry()
txt_mk.grid(row=1, column=1)

btn_login = Button(w, text="Login", command=check)
btn_login.grid(row=2, column=0)


btn_logout = Button(w, text="Logout")
btn_logout.grid(row=2, column=1)


w.mainloop()
