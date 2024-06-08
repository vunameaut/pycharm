from tkinter import *
from tkinter.ttk import Combobox

from PIL import Image, ImageTk
import random

w = Tk()
w.title("Test Image")
w.geometry("600x600")
# Tạo cửa sổ chính
def cau1():
    


    img_import = Image.open(r"D:/hoc tap/python/pycharm/buoi11_6_6_2024/mat.png")
    resize_img = img_import.resize((200, 200))


    img = ImageTk.PhotoImage(resize_img)

    def hien_thi():
        ten = entry_ten.get()
        danh_sach.insert(END, "welcome to " +ten)

    hinh_anh = Label(w, text='', image=img)
    hinh_anh.pack(pady=10)
    hinh_anh.image = img

    label_ten = Label(w, text='nhập vào tên của bạn')
    label_ten.pack(pady=10)

    entry_ten = Entry(w)
    entry_ten.pack(pady=10)

    nut = Button(w, text='Click here',command=hien_thi)
    nut.pack(pady=10)

    danh_sach = Listbox(w)
    danh_sach.pack(pady=10)


    w.mainloop()

def cau2():

    def check_kq():
        a = int(so_1.get())
        b = int(so_2.get())
        c = int(kq.get())
        if a + b == c:
            label_dung.config(image=img_tich)
        else:
            label_dung.config(image=img_gach)

    so_1 = Entry(w)
    so_1.insert(END, str(random.randint(1, 50)))
    so_1.grid(row=0, column=0, padx=10, pady=10)

    so_2 = Entry(w)
    so_2.insert(END, str(random.randint(1, 50)))
    so_2.grid(row=1, column=0, padx=10, pady=10)

    kq = Entry(w)
    kq.grid(row=2, column=0, padx=10, pady=10)

    btn_check = Button(w, text='Check', command=check_kq)
    btn_check.grid(row=2, column=1, padx=10, pady=10)

    btn_next = Button(w, text='Next')
    btn_next.grid(row=2, column=2, padx=10, pady=10)

    # Load hình ảnh vào bộ nhớ
    img_tich = PhotoImage(file="D:/hoc tap/python/pycharm/buoi11_6_6_2024/tich.png")
    img_gach = PhotoImage(file="D:/hoc tap/python/pycharm/buoi11_6_6_2024/gach.png")

    # Tạo Label để hiển thị hình ảnh
    label_dung = Label(w)
    label_dung.grid(row=3, column=0, columnspan=3, pady=10)

    w.mainloop()


def cau3():
    def doibg():
        mau = danh_sach.get()
        if mau == "xanh":
            w.config(bg="blue")
        elif mau == "đỏ":
            w.config(bg="red")
        elif mau == "vàng":
            w.config(bg="yellow")
        elif mau == "tím":
            w.config(bg="purple")
        elif mau == "hồng":
            w.config(bg="pink")
        else:
            w.config(bg="white")


    colors = ["xanh", "đỏ", "vàng", "tím", "hồng"]
    selected_color = StringVar()
    selected_color.set(colors[0])  # Mặc định chọn màu đầu tiên trong danh sách

    danh_sach = Combobox(w, textvariable=selected_color, values=colors)
    danh_sach.grid(row=0, column=0, padx=10, pady=10)

    btn_doibg = Button(w, text='Đổi màu', command=doibg)
    btn_doibg.grid(row=0, column=1, padx=10, pady=10)

    w.mainloop()

def cau4():
    def add_to_list():
        name = entry_name.get()
        gender = combo_gender.get()
        entry_name.delete(0, END)
        combo_gender.set("chọn giới tính")
        list_box.insert(END, f"{name}, {gender}")

    label_name = Label(w, text='nhập tê bạn :')
    label_name.grid(row=0, column=0, padx=10, pady=10)

    entry_name = Entry(w)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    label_gender = Label(w, text='chọn giới tính:')
    label_gender.grid(row=1, column=0, padx=10, pady=10)

    combo_gender = Combobox(w, values=['trai', 'gái', 'khó nói'])
    combo_gender.set("chọn giới tính")
    combo_gender.grid(row=1, column=1, padx=10, pady=10)

    button_add = Button(w, text='thêm vào list', command=add_to_list)
    button_add.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    list_box = Listbox(w)
    list_box.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    w.mainloop()

def cau5():
    def add_to_list():
            name = entry_name.get()
            gender = combo_gender.get()
            entry_name.delete(0, END)
            combo_gender.set("chọn giới tính")
            list_box.insert(END, f"{name}, {gender}")
            write_to_file(f"{name}, {gender}")

    def write_to_file(data):
            with open("data.txt", "a") as file:
                file.write(data + "\n")

    def display_file():
            with open("data.txt", "r") as file:
                content = file.read()
                print(content)

    label_name = Label(w, text='nhập tê bạn :')
    label_name.grid(row=0, column=0, padx=10, pady=10)

    entry_name = Entry(w)
    entry_name.grid(row=0, column=1, padx=10, pady=10)
    label_gender = Label(w, text='chọn giới tính:')
    label_gender.grid(row=1, column=0, padx=10, pady=10)

    combo_gender = Combobox(w, values=['trai', 'gái', 'khó nói'])
    combo_gender.set("chọn giới tính")
    combo_gender.grid(row=1, column=1, padx=10, pady=10)

    button_add = Button(w, text='thêm vào list', command=add_to_list)
    button_add.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    button_display = Button(w, text='hiển thị file', command=display_file)
    button_display.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    list_box = Listbox(w)
    list_box.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    w.mainloop()            

def cau6():
    def hien_thi():
        so = int(n.get())
        img_path = f"{so}.gif"
        img_import = Image.open(img_path)
        resize_img = img_import.resize((200, 200) )
        img = ImageTk.PhotoImage(resize_img)
        label_anh.config(image=img)
        label_anh.image = img
        n.delete(0,END)

    tn = Label(w, text = "Nhập vào số nguyên dương n: ")
    tn.grid(row = 0, column = 0, padx = 10, pady = 10)

    n = Entry()
    n.grid(row = 0, column = 1, padx = 10, pady = 10)

    hien_thi = Button(w, text = "Hiển thị", command = hien_thi)
    hien_thi.grid(row = 0, column = 2, padx = 10, pady = 10)

    label_anh = Label(w, text = "")
    label_anh.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10)

    w.mainloop()


while True:
    chon = int(input(text="nhập lựa chọn: "))
    match(chon):
        case 1:
            cau1()
        case 2:
            cau2()