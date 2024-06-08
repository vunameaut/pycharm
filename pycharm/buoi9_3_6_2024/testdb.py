
# import sqlite3
# from turtle import Screen
# path = "D:/hoc tap/python/data/qlgv.db"
# conn = sqlite3.connect(path)
# print(conn)

# w = Tk()
# c = Screen()
# def printAll(result):
#     for item in result:
#         print(item)

# # Create two entry widgets for username and password
# username_entry = w.Entry(c)
# password_entry = w.Entry(c, show="*")

#         # Position the entry widgets on the window
# username_entry.pack(pady=10)
# password_entry.pack(pady=10)        

# cursor = conn.cursor()
# cursor.execute("SELECT * FROM Dang_nhap where Tai_khoan = 'admin' and Mat_khau = 'admin'")
# result = cursor.fetchall()



# print(printAll(result))




# conn.close()

# from tkinter import *
# from PIL import Image, ImageTk
#
# # Tạo cửa sổ chính
# w = Tk()
# w.title("Test Image")
# w.geometry("400x600")
#
# # Mở và thay đổi kích thước hình ảnh
# img_import = Image.open(r'D:\a.png')
# resize = img_import.resize((300, 300), Image.ANTIALIAS)
#
# # Tạo đối tượng PhotoImage từ hình ảnh đã thay đổi kích thước
# img = ImageTk.PhotoImage(resize)
#
# # Tạo nút với hình ảnh
# hinh_anh = Button(w, text='', image=img)
# hinh_anh.place(x=50, y=50)
#
# # Giữ tham chiếu tới đối tượng PhotoImage để tránh bị thu hồi
# hinh_anh.image = img
#
# # Bắt đầu vòng lặp chính
# w.mainloop()
import tkinter as tk
from tkinter import Button, Tk, messagebox

def show_values():
    print(f"Checkbutton: {check_var.get()}")
    print(f"Radiobutton: {radio_var.get()}")
    print(f"Scale: {scale_var.get()}")
    print(f"Spinbox: {spinbox_var.get()}")
    print(f"OptionMenu: {option_var.get()}")

# Hàm xử lý sự kiện khi chọn menu
def menu_action():
    messagebox.showinfo("Menu", "Menu item clicked!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tkinter Widget Examples")
root.geometry("400x400")

# Checkbutton
check_var = tk.IntVar()
check_button = tk.Checkbutton(root, text="Check me", variable=check_var)
check_button.pack(pady=10)

# Radiobutton
radio_var = tk.IntVar()
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value=1)
radio_button2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value=2)
radio_button1.pack(pady=10)
radio_button2.pack(pady=10)

# Scale
scale_var = tk.IntVar()
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, variable=scale_var)
scale.pack(pady=10)

# Spinbox
spinbox_var = tk.IntVar()
spinbox = tk.Spinbox(root, from_=0, to=10, textvariable=spinbox_var)
spinbox.pack(pady=10)

# OptionMenu
options = ["Option A", "Option B", "Option C"]
option_var = tk.StringVar()
option_var.set(options[0])  # Thiết lập giá trị mặc định
option_menu = tk.OptionMenu(root, option_var, *options)
option_menu.pack(pady=10)

# Menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=menu_action)
file_menu.add_command(label="Save", command=menu_action)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=menu_action)
edit_menu.add_command(label="Copy", command=menu_action)
edit_menu.add_command(label="Paste", command=menu_action)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)

# Nút hiển thị giá trị
show_button = tk.Button(root, text="Show Values", command=show_values)
show_button.pack(pady=20)

# Bắt đầu vòng lặp chính
root.mainloop()



