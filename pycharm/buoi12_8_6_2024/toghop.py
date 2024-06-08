from cmath import sqrt
from tkinter import *


from PIL import Image,ImageTk

w = Tk()

def cau1():
    def giaiptb1():
        a = int(txt_a.get())
        b = int(txt_b.get())

        if a == 0:
            if b == 0:
                kq.insert(END, "phương trình vô số nghiệm\n ")
            else:
                kq.insert(END, "phương trình vô nghiệm\n")
        else:
            x = -b / a
            kq.insert(END, " x= " + str(x))

    def giaiptb2():
        a = int(txt_a.get())
        b = int(txt_b.get())
        c = int(txt_c.get())
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            kq.insert(END, "phương trình vô nghiệm\n")
        elif delta == 0:
            x = -b / (2 * a)
            kq.insert(END, " x= " + str(x))
        else:
            x1 = (-b + sqrt(delta)) / (2 * a)
            x2 = (-b - sqrt(delta)) / (2 * a)
            kq.insert(END, " x1= " + str(x1) + " \n x2= " + str(x2))

        

    nhap_a = Label(w,text="nhap a")
    nhap_a.grid(row=0, column=0, padx=10, pady=10)

    nhap_b = Label(w,text="nhap b")
    nhap_b.grid(row=1, column=0, padx=10 , pady=10)

    nhap_c = Label(w,text="nhap c")
    nhap_c.grid(row=2, column=0, padx=10, pady=10)

    txt_a = Entry(w)
    txt_a.grid(row=0, column=1, padx=10, pady=10)

    txt_b = Entry(w)
    txt_b.grid(row=1, column=1, padx=10, pady=10)

    txt_c = Entry(w)
    txt_c.grid(row=2, column=1, padx=10, pady=10)

    ptb2 = Button(text="Giai ptb2",command=giaiptb2)
    ptb2.grid(row=3, column=0, padx=10, pady=10)

    ptbn = Button(text="Giai ptbn",command=giaiptb1)
    ptbn.grid(row=3, column=1, padx=10, pady=10)

    kq = Listbox(w)
    kq.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    w.mainloop()


def cau2():
    def add_to_list():
        number = entry.get()
        if number.isdigit():
            result_list.insert(END, number)
            entry.delete(0, END)
        else:
            entry.delete(0, END)

    def clear_list():
        result_list.delete(0, END)

    def save_to_file():
        with open("so.csv", "w") as file:
            for item in result_list.get(0, END):
                file.write(item + "\n")
        status_label.config(text="Lưu thành công")

    def exit_program():
        w.quit()

    def update_image(*args):
        selected_option = option_var.get()
        image = image_dict.get(selected_option)
        resized_image = image.resize((200, 200))
        if image:
            photo = ImageTk.PhotoImage(resized_image)
            image_label.config(image=photo)
            image_label.image = photo


    instruction_label = Label(w, text="Nhập số vào đây:")
    instruction_label.grid(row=0, column=0, padx=10, pady=10)

    entry = Entry(w)
    entry.grid(row=0, column=1, padx=10, pady=10)

    add_button = Button(w, text="Thêm vào danh sách", command=add_to_list)
    add_button.grid(row=0, column=2, padx=10, pady=10)

    clear_button = Button(w, text="Xóa danh sách", command=clear_list)
    clear_button.grid(row=2, column=2, padx=10, pady=10)

    save_button = Button(w, text="Lưu vào danh sách", command=save_to_file)
    save_button.grid(row=3, column=2, padx=10, pady=10)

    exit_button = Button(w, text="Thoát", command=exit_program)
    exit_button.grid(row=4, column=2, padx=10, pady=10)

    status_label = Label(w, text="")
    status_label.grid(row=3, column=1, padx=10, pady=10)

    result_list = Listbox(w)
    result_list.grid(row=2, column=1, padx=10, pady=10)

    # OptionMenu
    options = ["Vũ Hoài Nam", "Nhật Bản", "Canada"]
    option_var = StringVar()
    option_var.set(options[0])
    option_var.trace('w', update_image)
    option_menu = OptionMenu(w, option_var, *options)
    option_menu.grid(row=1, column=1, padx=10, pady=10)

    # Load images
    image_dict = {
        "Vũ Hoài Nam": Image.open("mat.png"),
        "Nhật Bản": Image.open("nhatban.png"),
        "Canada": Image.open("canada.png")
    }

    # Image label
    image_label = Label(w)
    image_label.grid(row=1, column=0, padx=10, pady=10)

    # Initial image display
    update_image()

    w.mainloop()


cau2()