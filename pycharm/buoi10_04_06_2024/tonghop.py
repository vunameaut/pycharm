import random
from tkinter import *
from tkinter import messagebox
from turtle import  *

w= Tk()
w.title("bài tập buổi 10")
w.geometry("500x500")

def cau1():
    def tong():
        a = int(entry_a.get())
        b = int(entry_b.get())
        ketqua = a + b
        entry_ketqua.delete(0, END)
        entry_ketqua.insert(0, ketqua)

    def hieu():
        a = int(entry_a.get())
        b = int(entry_b.get())
        ketqua = a - b
        entry_ketqua.delete(0, END)
        entry_ketqua.insert(0, ketqua)

    def tich():
        a = int(entry_a.get())
        b = int(entry_b.get())
        ketqua = a * b
        entry_ketqua.delete(0, END)
        entry_ketqua.insert(0, ketqua)

    def thuong():
        a = int(entry_a.get())
        b = int(entry_b.get())
        ketqua = a / b
        entry_ketqua.delete(0, END)
        entry_ketqua.insert(0, ketqua)

    def huy():
        w.destroy()

    def xoa_thong_tin():
        entry_a.delete(0, END)
        entry_b.delete(0, END)
        entry_ketqua.delete(0, END)
        list_hoatdong.delete(0, END)

    def hien_thi(button):
        a = entry_a.get()
        b = entry_b.get()
        ketqua = entry_ketqua.get()
        button_text = button.cget("text")
        list_hoatdong.insert(END, f"{a} {button_text} {b} = {ketqua}")

    label_a = Label(text="Nhập vào số a: ",bd=2,relief="solid")
    label_b = Label(text="Nhập vào số b: ",bd=2,relief="solid")
    label_ketqua = Label(text="Kết quả: ",bd=2,relief="solid")

    entry_a = Entry(bg="yellow",fg="green")
    entry_b = Entry(bg="yellow",fg="green")
    entry_ketqua = Entry(bg="yellow",fg="green")

    list_hoatdong = Listbox(bd=5,relief="solid")

    button_tong = Button(text="+",command=lambda:(tong(),hien_thi(button_tong)))
    button_hieu = Button(text="-",command=lambda:(hieu(),hien_thi(button_hieu)))
    button_tich = Button(text="*",command=lambda:(tich(),hien_thi(button_tich)))
    button_thuong = Button(text="/",command=lambda:(thuong(),hien_thi(button_thuong)))
    button_xoa = Button(text="Xóa",command=xoa_thong_tin)
    button_exit = Button(text="Thoát",command=huy)

    label_a.grid(row=0, column=0,padx=10,pady=10)
    label_b.grid(row=1, column=0,padx=10,pady=10)
    label_ketqua.grid(row=2, column=0,padx=10,pady=10)

    entry_a.grid(row=0, column=1,padx=10,pady=10)
    entry_b.grid(row=1, column=1,padx=10,pady=10)
    entry_ketqua.grid(row=2, column=1,padx=10,pady=10)

    list_hoatdong.grid(row=0, column=2, rowspan=3, columnspan=2,padx=10,pady=10)

    button_tong.grid(row=3, column=0,padx=10,pady=10)
    button_hieu.grid(row=3, column=1,padx=10,pady=10)
    button_tich.grid(row=3, column=2,padx=10,pady=10)
    button_thuong.grid(row=3, column=3,padx=10,pady=10)
    button_xoa.grid(row=4, column=0,padx=10,pady=10)
    button_exit.grid(row=4, column=1,padx=10,pady=10)

    w.mainloop()    

def cau2():
    def tinhgiathua():
        a = random.randint(1, 100)  
        ketqua = 1
        for i in range(1, a + 1):
            ketqua = ketqua * i
        list_ket_qua.delete(0, END)
        list_ket_qua.insert(0, ketqua)

    def thtt():
        a = random.randint(1, 100)  
        b = random.randint(1, 100) 

        tong = a + b
        hieu = a - b
        tich = a * b
        thuong = a / b
        list_ket_qua.delete(0, END)
        list_ket_qua.insert(0, f"{tong} {hieu} {tich} {thuong}")

    def ptbn():
        a = random.randint(1, 100)  
        b = random.randint(1, 100) 
        if b == 0:
            list_ket_qua.delete(0, END)
            list_ket_qua.insert(0, "phương trình vô nghiệm")
        else:
            list_ket_qua.delete(0, END)
            list_ket_qua.insert(0, f"-{b}x + {a} = 0")

    def fourhdt():
        a = random.randint(1, 100)  
        b = random.randint(1, 100) 
        ketqua1 ="( a + b )2"+ a**2 + 2*a*b + b**2
        ketqua2 ="( a - b )2"+ a**2 - 2*a*b + b**2
        ketqua3 ="a2 - b2"+ (a**2 - b**2)
        ketqua4 ="( a + b )3"+ (a + b)**3
        list_ket_qua.delete(0, END)
        for i in [ketqua1, ketqua2, ketqua3, ketqua4]:
            list_ket_qua.insert(END, i)

    def vetamgiacABC():
        
        w = Screen()
        c = Turtle()
        c.speed(5)

         # Di chuyển và vẽ cạnh AB
        c.penup()
        c.goto(-50, 0)
        c.pendown()
        c.write("A", font=("Arial", 12, "normal"))
        c.forward(100)

        # Di chuyển và vẽ cạnh BC
        c.penup()
        c.goto(50, 0)
        c.pendown()
        c.write("B", font=("Arial", 12, "normal"))
        c.left(120)
        c.forward(100)

        # Di chuyển và vẽ cạnh CA
        c.penup()
        c.goto(-2, 84)
        c.pendown()
        c.write("C", font=("Arial", 12, "normal"))
        c.left(120)
        c.forward(100)

        w.mainloop()
    def vemaytinha():
        w = Screen()
        c = Turtle()
        c.speed(5)

        # Vẽ hình bình hành thứ nhất
        c.penup()
        c.goto(-100, 0)
        c.pendown()
        c.forward(100)
        c.left(120)
        c.forward(100)
        c.left(60)
        c.forward(100)
        c.left(120)
        c.forward(100)

        # Vẽ hình bình hành thứ hai
        c.penup()
        c.goto(100, 0)
        c.pendown()
        c.forward(100)
        c.right(120)
        c.forward(100)
        c.right(60)
        c.forward(100)
        c.right(120)
        c.forward(100)

        w.mainloop()
    def huy():
        w.destroy()

    label1 = Label(w, text="Nhập số a:")
    label1.grid(row=0, column=0, padx=10, pady=10)

    label2 = Label(w, text="Nhập số b:")
    label2.grid(row=1, column=0, padx=10, pady=10)

    list_ket_qua = Listbox(w)
    list_ket_qua.grid(row=2, column=3, columnspan=2, padx=10, pady=10)

    entry1 = Entry(w, bg="yellow", fg="green")
    entry1.grid(row=0, column=1, padx=10, pady=10)

    entry2 = Entry(w, bg="yellow", fg="green")
    entry2.grid(row=1, column=1, padx=10, pady=10)

    tinhgiaithua = Button(w, text="tính giai thừa của a", command=tinhgiathua)
    tinhgiaithua.grid(row=2, column=0, padx=10, pady=10)

    thtt = Button(w, text="tính tổng hiệu tích thương", command=thtt)
    thtt.grid(row=2, column=1, padx=10, pady=10)

    ptbn = Button(w, text="phương trình bậc nhất", command=ptbn)
    ptbn.grid(row=3, column=0, padx=10, pady=10)

    fourhdt = Button(w, text="4 hằng đẳng thức", command=fourhdt)
    fourhdt.grid(row=3, column=1, padx=10, pady=10)

    vetamgiac = Button(w, text="vẽ tam giác",command=vemaytinha)
    vetamgiac.grid(row=4, column=0, padx=10, pady=10)

    vemaytinh = Button(w, text="vẽ máy tính ")
    vemaytinh.grid(row=4, column=1, padx=10, pady=10)

    thoat = Button(w, text="thoát", command=huy)
    thoat.grid(row=5, column=0, padx=10, pady=10)

    w.mainloop()

def cau3():

    def hien_thi():
        a = entry_ten.get()
        b = entry_tuoi.get()
        c = entry_gioitinh.get()
        d = entry_diachi.get()
        e = entry_sdt.get()
        f = entry_email.get()
        for item in [a, b, c, d, e, f]:
            list_thongtin.insert(END, item)
    def nhap_thong_tin():
        if entry_ten.get() == "" or entry_tuoi.get() == "" or entry_gioitinh.get() == "" or entry_diachi.get() == "" or entry_sdt.get() == "" or entry_email.get() == "":
            messagebox.showerror("Lỗi","Nhập thông tin thất bại")
        else:
            messagebox.showinfo("Thành công","Nhập thông tin thành công")
    def thoat():
        exit()
    #tạo form nhập thông tin cá nhân
    ten = Label(w,text="Họ và tên: ",bd=2,relief="solid")
    ten.grid(row=0,column=0,padx=10,pady=10)
    tuoi = Label(w,text="Tuổi: ",bd=2,relief="solid")
    tuoi.grid(row=1,column=0,padx=10,pady=10)
    gioitinh = Label(w,text="Giới tính: ",bd=2,relief="solid")
    gioitinh.grid(row=2,column=0,padx=10,pady=10)
    diachi = Label(w,text="Địa chỉ: ",bd=2,relief="solid")
    diachi.grid(row=3,column=0,padx=10,pady=10)
    sdt = Label(w,text="Số điện thoại: ",bd=2,relief="solid")
    sdt.grid(row=4,column=0,padx=10,pady=10)
    email = Label(w,text="Email: ",bd=2,relief="solid")
    email.grid(row=5,column=0,padx=10,pady=10)

    #tạo entry để nhập thông tin
    entry_ten = Entry()
    entry_ten.grid(row=0,column=1,padx=10,pady=10)
    entry_tuoi = Entry()
    entry_tuoi.grid(row=1,column=1,padx=10,pady=10)
    entry_gioitinh = Entry()
    entry_gioitinh.grid(row=2,column=1,padx=10,pady=10)
    entry_diachi = Entry()
    entry_diachi.grid(row=3,column=1,padx=10,pady=10)
    entry_sdt = Entry()
    entry_sdt.grid(row=4,column=1,padx=10,pady=10)
    entry_email = Entry()
    entry_email.grid(row=5,column=1,padx=10,pady=10)
    

    #tạo listbox để hiển thị thông tin
    list_thongtin = Listbox( )
    list_thongtin.grid(row=0,column=2,rowspan=6,columnspan=2,padx=10,pady=10)

    #tạo button hiển thị thong tin da nhap vao list
    button_hien_thi = Button(text="Hiển thị thông tin",command=hien_thi)
    button_hien_thi.grid(row=6,column=0,padx=10,pady=10)

    #nếu không có ô entry nào trống thì thông báo ra là nhập thành công không thì sẽ thông báo là nhập thất bại
    button_nhap = Button(text="Nhập thông tin",command=nhap_thong_tin)
    button_nhap.grid(row=6,column=1,padx=10,pady=10)
    button_thoat = Button(text="Thoát",command=thoat)
    button_thoat.grid(row=6,column=2,padx=10,pady=10)
    w.mainloop()

cau2()
    