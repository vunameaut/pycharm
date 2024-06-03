from tkinter import *
from tkinter import messagebox

w = Tk()
w.title("bài tập buổi 9")
w.geometry("300x300")
def cau1():
    def laydata_ten():
        ten = entry_ten.get()
        label_ketqua.config(text="xin chào" + " " + ten)

    label = Label(text="nhập vào tên bạn")
    label.place(x=20, y=20, width=100, height=25)

    entry_ten = Entry()
    entry_ten.place(x=150, y=20, width=100, height=25)

    laydata_ten = Button(text="click here", command=laydata_ten)
    laydata_ten.place(x=20, y=90, width=100, height=25)

    label_ketqua = Label(text="")
    label_ketqua.place(x=20, y=190, width=100, height=25)

    w.mainloop()
def cau2():
    def random():
        import random
        roll=random.randint(1, 6)
        label.config(text=roll)


    label = Label(text="0")
    label.place(x=20, y=20, width=100, height=25)

    button = Button(text="roll",command=random)
    button.place(x=20, y=150, width=100, height=25)

    w.mainloop()




def cau3():

    total_sum = 0

    def thoat():
        exit()

    def storeNumber():
        global total_sum
        nummm = entry_Box.get()
        total_sum += int(nummm)
        entry_Box.delete(0, END)
        result_Label.config(text=total_sum)

    def clearNumbers():
        global total_sum
        total_sum = 0
        result_Label.config(text="0")

    # Input
    label_Entry_Box = Label(text="Enter number: ")
    label_Entry_Box.place(x=0, y=30, width=150, height=30)
    entry_Box = Entry()
    entry_Box.place(x=130, y=30, width=150, height=30)

    button_Add = Button(text="Add", command=storeNumber)
    button_Add["bg"] = "black"
    button_Add["fg"] = "white"
    button_Add.place(x=300, y=30, width=100, height=30)

    button_Clear = Button(text="Clear", command=clearNumbers)
    button_Clear["bg"] = "black"
    button_Clear["fg"] = "white"
    button_Clear.place(x=300, y=70, width=100, height=30)

    # Output
    label_Entry_Box = Label(text="Answer: ")
    label_Entry_Box.place(x=0, y=70, width=150, height=30)
    result_Label = Label(text="0", bg="light gray", fg="black")
    result_Label.place(x=130, y=70, width=150, height=30)

    # Exit
    button_Thoat = Button(text="Exit", command=thoat)
    button_Thoat["bg"] = "black"
    button_Thoat["fg"] = "white"
    button_Thoat.place(x=30, y=200, width=100, height=50)

    w.mainloop()


def cau4():

    def list():
        ten = nguon_nhap.get()
        nhom_ketqua.insert(END,ten)
        nguon_nhap.delete(0, END)


    nhan_dan = Label(text="Nhập tên vào đây:")
    nhan_dan.pack(pady=10)

    nguon_nhap = Entry()
    nguon_nhap.pack(pady=5)

    them = Button(text="Thêm tên vào danh sách ", command=list)
    them.pack(pady=5)

    nhom_ketqua = Listbox()
    nhom_ketqua.pack(pady=6)


    w.mainloop()
def cau5():
    def km_to_miles():
        km = float(input.get())
        miles = km * 0.621371
        output.delete(0, END)
        output.insert(END,str(miles))


    def miles_to_km():
        miles = float(input.get())
        km = miles / 0.621371
        output.delete(0, END)
        output.insert(END,str(km))


    label = Label(text="Nhập vào giá trị dưới đây để đổi ")
    label.pack(pady=10)

    input = Entry()
    input.pack(pady=5)

    km_to_miles= Button(text="Km sang miles",command=km_to_miles)
    km_to_miles.pack(pady=5)

    miles_to_km = Button(text="miles sang km ",command=miles_to_km)
    miles_to_km.pack(pady=5)

    output = Entry()
    output.pack(pady=5)
    w.mainloop()

def cau6():
    def list():
        ten = nguon_nhap.get()
        if ten.isdigit():
            nhom_ketqua.insert(END, ten)
            nguon_nhap.delete(0, END)
        else:
            nguon_nhap.delete(0, END)

    nhan_dan = Label(text="Nhập số vào đây:")
    nhan_dan.pack(pady=10)

    nguon_nhap = Entry()
    nguon_nhap.pack(pady=5)

    them = Button(text="Thêm vào danh sách ", command=list)
    them.pack(pady=5)

    nhom_ketqua = Listbox()
    nhom_ketqua.pack(pady=6)

    w.mainloop()


def cau7():
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

    luu_file = Button(text="luu thanh file dạng csv ",command=luu)
    luu_file.pack(pady=5)

    nhom_ketqua = Listbox()
    nhom_ketqua.pack(pady=6)



    w.mainloop()
def cau8():

    def lammoi():
        ten.delete(0, END)
        tuoi.delete(0, END)
    def themthongtin():
        file=open("ten_tuoi.csv","w")
        file.write(ten.get()+","+tuoi.get())
        file.close()
        file=open("ten_tuoi.csv","r")
        print(file.read())
        file.close()
        ten.delete(0, END)
        tuoi.delete(0, END)
        messagebox.showinfo("thông báo","thêm thành công")


    label1=Label(text="Nhập vao ten cua ban")
    label1.pack(pady=5)

    ten=Entry()
    ten.pack(pady=5)

    label2=Label(text="nhap vao tuoi cua ban")
    label2.pack(pady=5)

    tuoi = Entry()
    tuoi.pack(pady=5)

    nhap_moi= Button(text="Nhập mới",command=lammoi)
    nhap_moi.pack(pady=5)

    them=Button(text="Thêm thông tin ",command=themthongtin)
    them.pack(pady=5)
    w.mainloop()
def cau9():
    def lammoi():
        ten.delete(0, END)
        tuoi.delete(0, END)
        danhsach.delete(0, END)

    def themthongtin():
        file = open("ten_tuoi.csv","a")
        file.write(ten.get()+","+tuoi.get()+"\n")
        file.close()
        file = open("ten_tuoi.csv", "r")
        print(file.read())
        file.close()

        ten.delete(0, END)
        tuoi.delete(0, END)
        danhsach.delete(0, END)
        messagebox.showinfo("thông báo", "thêm thành công")

    def lammoidanhsach():
        danhsach.delete(0, END)
        with open("ten_tuoi.csv", "r") as file:
            lines = file.readlines()  # Đọc từng dòng trong file
            for line in lines:
                danhsach.insert(END, line.strip())

    label1 = Label(text="Nhập vao ten cua ban")
    label1.pack(pady=5)

    ten = Entry()
    ten.pack(pady=5)

    label2 = Label(text="nhap vao tuoi cua ban")
    label2.pack(pady=5)

    tuoi = Entry()
    tuoi.pack(pady=5)

    nhap_moi = Button(text="Nhập mới", command= lambda :(lammoi() , lammoidanhsach()))
    nhap_moi.pack(pady=5)

    them = Button(text="Thêm thông tin ", command=lambda :(themthongtin(), lammoidanhsach()))
    them.pack(pady=5)

    danhsach= Listbox()
    danhsach.pack(pady=6)

    w.mainloop()


while True:

    chon=int(input("nhập vào lựa chọn của bạn: "))
    match(chon):
        case 1:
            cau1()
        case 2:
            cau2()
        case 3:
            cau3()
        case 4:
            cau4()
        case 5:
            cau5()
        case 6:
            cau6()
        case 7:
            cau7()
        case 8:
            cau8()
        case 9:
            cau9()