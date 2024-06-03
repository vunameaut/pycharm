from tkinter import *

tong = 0

def cong_vao_tong():
    global tong
    try:
        num = int(nguon_nhap.get())
        tong += num
        nhom_ketqua.config(text=str(tong))
        nguon_nhap.delete(0, END)
    except ValueError:
        nhom_ketqua.config(text="Vui lòng nhập số hợp lệ")

def dat_lai_tong():
    global tong
    tong = 0
    nhom_ketqua.config(text=str(tong))
    nguon_nhap.delete(0, END)

w = Tk()
w.title("Cộng dồn số")
w.geometry("300x200")

nhan_dan = Label(w, text="Nhập số vào đây:")
nhan_dan.pack(pady=10)

nguon_nhap = Entry(w)
nguon_nhap.pack(pady=5)

nut_cong = Button(w, text="Cộng vào tổng", command=cong_vao_tong)
nut_cong.pack(pady=5)

nhom_ketqua = Label(w, text=str(tong), borderwidth=2, relief="solid")
nhom_ketqua.pack(pady=10)

nut_dat_lai = Button(w, text="Đặt lại tổng", command=dat_lai_tong)
nut_dat_lai.pack(pady=5)

w.mainloop()
