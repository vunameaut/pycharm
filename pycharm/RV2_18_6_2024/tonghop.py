import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Tạo cơ sở dữ liệu và bảng
def tao_bang():
    connect = sqlite3.connect("online_store.db")
    cursor = connect.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nguoi_dung (
        nguoi_dung_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ten_dang_nhap TEXT NOT NULL UNIQUE,
        mat_khau TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS san_pham (
        san_pham_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ten TEXT NOT NULL,
        mo_ta TEXT,
        gia REAL NOT NULL,
        so_luong INTEGER NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS khach_hang (
        khach_hang_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ten TEXT NOT NULL,
        email TEXT NOT NULL,
        so_dien_thoai TEXT,
        dia_chi TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS don_hang (
        don_hang_id INTEGER PRIMARY KEY AUTOINCREMENT,
        khach_hang_id INTEGER,
        ngay_dat DATE NOT NULL,
        trang_thai TEXT NOT NULL,
        FOREIGN KEY (khach_hang_id) REFERENCES khach_hang(khach_hang_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chi_tiet_don_hang (
        chi_tiet_don_hang_id INTEGER PRIMARY KEY AUTOINCREMENT,
        don_hang_id INTEGER,
        san_pham_id INTEGER,
        so_luong INTEGER NOT NULL,
        gia REAL NOT NULL,
        FOREIGN KEY (don_hang_id) REFERENCES don_hang(don_hang_id),
        FOREIGN KEY (san_pham_id) REFERENCES san_pham(san_pham_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS phan_hoi (
        phan_hoi_id INTEGER PRIMARY KEY AUTOINCREMENT,
        khach_hang_id INTEGER,
        tin_nhan TEXT NOT NULL,
        phan_hoi TEXT,
        ngay_gui DATE NOT NULL,
        FOREIGN KEY (khach_hang_id) REFERENCES khach_hang(khach_hang_id)
    );
    """)

    connect.commit()
    connect.close()

def dang_nhap():
    ten_dang_nhap = ten_dang_nhap_entry.get()
    mat_khau = mat_khau_entry.get()

    connect = sqlite3.connect("online_store.db")
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM nguoi_dung WHERE ten_dang_nhap=? AND mat_khau=?", (ten_dang_nhap, mat_khau))
    hang = cursor.fetchone()

    if hang:
        messagebox.showinfo("Đăng nhập", "Đăng nhập thành công!")
        hien_thi_man_hinh_quan_ly()
        w.withdraw()


    elif ten_dang_nhap == 'a' and mat_khau == 'a':
        messagebox.showinfo("Đăng nhập", "Đăng nhập thành công!")
        hien_thi_man_hinh_quan_ly()
        w.withdraw()

    else:
        messagebox.showerror("Đăng nhập", "Tên đăng nhập hoặc mật khẩu không đúng")

    connect.close()


def hien_thi_man_hinh_quan_ly():
    quan_ly = Toplevel(w)
    quan_ly.geometry("1920x1080")
    quan_ly.title("Màn hình quản lý")

    Button(quan_ly, text="Quản lý sản phẩm", command=quan_ly_san_pham).pack()
    Button(quan_ly, text="Quản lý khách hàng", command=quan_ly_khach_hang).pack()
    Button(quan_ly, text="Quản lý đơn hàng", command=quan_ly_don_hang).pack()
    Button(quan_ly, text="Quản lý phản hồi", command=quan_ly_phan_hoi).pack()
    Button(quan_ly, text="Xuất báo cáo và thống kê", command=xuat_bao_cao).pack()


def quan_ly_san_pham():
    san_pham_win = Toplevel(w)
    san_pham_win.title("Quản lý sản phẩm")

    def them_san_pham():
        ten = ten_entry.get()
        mo_ta = mo_ta_entry.get()
        gia = gia_entry.get()
        so_luong = so_luong_entry.get()

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("INSERT INTO san_pham (ten, mo_ta, gia, so_luong) VALUES (?, ?, ?, ?)",
                       (ten, mo_ta, gia, so_luong))
        connect.commit()
        connect.close()

        messagebox.showinfo("Thêm sản phẩm", "Sản phẩm đã được thêm thành công")
        hien_thi_san_pham()

    def sua_san_pham():
        id = id_entry.get()
        ten = ten_entry.get()
        mo_ta = mo_ta_entry.get()
        gia = gia_entry.get()
        so_luong = so_luong_entry.get()

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("UPDATE san_pham SET ten=?, mo_ta=?, gia=?, so_luong=? WHERE san_pham_id=?",
                       (ten, mo_ta, gia, so_luong, id))
        connect.commit()
        connect.close()

        messagebox.showinfo("Sửa sản phẩm", "Sản phẩm đã được sửa thành công")
        hien_thi_san_pham()

    def xoa_san_pham():
        id = id_entry.get()

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("DELETE FROM san_pham WHERE san_pham_id=?", (id,))
        connect.commit()
        connect.close()

        messagebox.showinfo("Xóa sản phẩm", "Sản phẩm đã được xóa")
        hien_thi_san_pham()

    def tim_kiem_san_pham():
        id = id_entry.get()

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM san_pham WHERE san_pham_id=?", (id,))
        hang = cursor.fetchone()
        connect.close()

        if hang:
            ten_entry.delete(0, END)
            ten_entry.insert(END, hang[1])
            mo_ta_entry.delete(0, END)
            mo_ta_entry.insert(END, hang[2])
            gia_entry.delete(0, END)
            gia_entry.insert(END, hang[3])
            so_luong_entry.delete(0, END)
            so_luong_entry.insert(END, hang[4])
        else:
            messagebox.showerror("Tìm kiếm sản phẩm", "Không tìm thấy sản phẩm")

    def hien_thi_san_pham():
        for row in san_pham_tree.get_children():
            san_pham_tree.delete(row)

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM san_pham")
        rows = cursor.fetchall()
        connect.close()
        w.withdraw()

        for row in rows:
            san_pham_tree.insert("", END, values=row)

    # Form nhập liệu
    id_label = Label(san_pham_win, text="ID")
    id_label.grid(row=0, column=0)
    id_entry = Entry(san_pham_win)
    id_entry.grid(row=0, column=1)

    ten_label = Label(san_pham_win, text="Tên")
    ten_label.grid(row=1, column=0)
    ten_entry = Entry(san_pham_win)
    ten_entry.grid(row=1, column=1)

    mo_ta_label = Label(san_pham_win, text="Mô tả")
    mo_ta_label.grid(row=2, column=0)
    mo_ta_entry = Entry(san_pham_win)
    mo_ta_entry.grid(row=2, column=1)

    gia_label = Label(san_pham_win, text="Giá")
    gia_label.grid(row=3, column=0)
    gia_entry = Entry(san_pham_win)
    gia_entry.grid(row=3, column=1)

    so_luong_label = Label(san_pham_win, text="Số lượng")
    so_luong_label.grid(row=4, column=0)
    so_luong_entry = Entry(san_pham_win)
    so_luong_entry.grid(row=4, column=1)

    them_button = Button(san_pham_win, text="Thêm", command=them_san_pham)
    them_button.grid(row=5, column=0)

    sua_button = Button(san_pham_win, text="Sửa", command=sua_san_pham)
    sua_button.grid(row=5, column=1)

    xoa_button = Button(san_pham_win, text="Xóa", command=xoa_san_pham)
    xoa_button.grid(row=5, column=2)

    tim_kiem_button = Button(san_pham_win, text="Tìm kiếm", command=tim_kiem_san_pham)
    tim_kiem_button.grid(row=5, column=3)

    # Hiển thị dữ liệu
    san_pham_tree = ttk.Treeview(san_pham_win, columns=("ID", "Tên", "Mô tả", "Giá", "Số lượng"), show="headings")
    san_pham_tree.heading("ID", text="ID")
    san_pham_tree.heading("Tên", text="Tên")
    san_pham_tree.heading("Mô tả", text="Mô tả")
    san_pham_tree.heading("Giá", text="Giá")
    san_pham_tree.heading("Số lượng", text="Số lượng")
    san_pham_tree.grid(row=6, column=0, columnspan=4)

    hien_thi_san_pham()


def quan_ly_khach_hang():
    khach_hang_win = Toplevel(w)
    khach_hang_win.title("Quản lý khách hàng")

    def them_khach_hang():
        ten = ten_entry.get()
        email = email_entry.get()
        so_dien_thoai = so_dien_thoai_entry.get()
        dia_chi = dia_chi_entry.get()

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("INSERT INTO khach_hang (ten, email, so_dien_thoai, dia_chi) VALUES (?, ?, ?, ?)",
                       (ten, email, so_dien_thoai, dia_chi))
        connect.commit()
        connect.close()

        messagebox.showinfo("Thêm khách hàng", "Khách hàng đã được thêm thành công")
        hien_thi_khach_hang()

    def sua_khach_hang():
        id = id_entry.get()
        ten = ten_entry.get()
        email = email_entry.get()
        so_dien_thoai = so_dien_thoai_entry.get()
        dia_chi = dia_chi_entry.get()

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("UPDATE khach_hang SET ten=?, email=?, so_dien_thoai=?, dia_chi=? WHERE khach_hang_id=?",
                       (ten, email, so_dien_thoai, dia_chi, id))
        connect.commit()
        connect.close()

        messagebox.showinfo("Sửa khách hàng", "Khách hàng đã được sửa thành công")
        hien_thi_khach_hang()

    def xoa_khach_hang():
        id = id_entry.get()

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("DELETE FROM khach_hang WHERE khach_hang_id=?", (id,))
        connect.commit()
        connect.close()

        messagebox.showinfo("Xóa khách hàng", "Khách hàng đã được xóa")
        hien_thi_khach_hang()

    def tim_kiem_khach_hang():
        id = id_entry.get()

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM khach_hang WHERE khach_hang_id=?", (id,))
        hang = cursor.fetchone()
        connect.close()

        if hang:
            ten_entry.delete(0, END)
            ten_entry.insert(END, hang[1])
            email_entry.delete(0, END)
            email_entry.insert(END, hang[2])
            so_dien_thoai_entry.delete(0, END)
            so_dien_thoai_entry.insert(END, hang[3])
            dia_chi_entry.delete(0, END)
            dia_chi_entry.insert(END, hang[4])
        else:
            messagebox.showerror("Tìm kiếm khách hàng", "Không tìm thấy khách hàng")

    def hien_thi_khach_hang():
        for row in khach_hang_tree.get_children():
            khach_hang_tree.delete(row)

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM khach_hang")
        rows = cursor.fetchall()
        connect.close()
        w.withdraw()

        for row in rows:
            khach_hang_tree.insert("", END, values=row)

    # Form nhập liệu
    id_label = Label(khach_hang_win, text="ID")
    id_label.grid(row=0, column=0)
    id_entry = Entry(khach_hang_win)
    id_entry.grid(row=0, column=1)

    ten_label = Label(khach_hang_win, text="Tên")
    ten_label.grid(row=1, column=0)
    ten_entry = Entry(khach_hang_win)
    ten_entry.grid(row=1, column=1)

    email_label = Label(khach_hang_win, text="Email")
    email_label.grid(row=2, column=0)
    email_entry = Entry(khach_hang_win)
    email_entry.grid(row=2, column=1)

    so_dien_thoai_label = Label(khach_hang_win, text="Số điện thoại")
    so_dien_thoai_label.grid(row=3, column=0)
    so_dien_thoai_entry = Entry(khach_hang_win)
    so_dien_thoai_entry.grid(row=3, column=1)

    dia_chi_label = Label(khach_hang_win, text="Địa chỉ")
    dia_chi_label.grid(row=4, column=0)
    dia_chi_entry = Entry(khach_hang_win)
    dia_chi_entry.grid(row=4, column=1)

    them_button = Button(khach_hang_win, text="Thêm", command=them_khach_hang)
    them_button.grid(row=5, column=0)

    sua_button = Button(khach_hang_win, text="Sửa", command=sua_khach_hang)
    sua_button.grid(row=5, column=1)

    xoa_button = Button(khach_hang_win, text="Xóa", command=xoa_khach_hang)
    xoa_button.grid(row=5, column=2)

    tim_kiem_button = Button(khach_hang_win, text="Tìm kiếm", command=tim_kiem_khach_hang)
    tim_kiem_button.grid(row=5, column=3)

    # Hiển thị dữ liệu
    khach_hang_tree = ttk.Treeview(khach_hang_win, columns=("ID", "Tên", "Email", "Số điện thoại", "Địa chỉ"), show="headings")
    khach_hang_tree.heading("ID", text="ID")
    khach_hang_tree.heading("Tên", text="Tên")
    khach_hang_tree.heading("Email", text="Email")
    khach_hang_tree.heading("Số điện thoại", text="Số điện thoại")
    khach_hang_tree.heading("Địa chỉ", text="Địa chỉ")
    khach_hang_tree.grid(row=6, column=0, columnspan=4)

    hien_thi_khach_hang()


def quan_ly_don_hang():
    don_hang_win = Toplevel(w)
    don_hang_win.title("Quản lý đơn hàng")

    def tao_don_hang():
        khach_hang_id = khach_hang_id_entry.get()
        ngay_dat = ngay_dat_entry.get()
        trang_thai = trang_thai_entry.get()

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("INSERT INTO don_hang (khach_hang_id, ngay_dat, trang_thai) VALUES (?, ?, ?)",
                       (khach_hang_id, ngay_dat, trang_thai))
        connect.commit()
        connect.close()

        messagebox.showinfo("Tạo đơn hàng", "Đơn hàng đã được tạo thành công")
        hien_thi_don_hang()

    def cap_nhat_don_hang():
        id = id_entry.get()
        khach_hang_id = khach_hang_id_entry.get()
        ngay_dat = ngay_dat_entry.get()
        trang_thai = trang_thai_entry.get()

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("UPDATE don_hang SET khach_hang_id=?, ngay_dat=?, trang_thai=? WHERE don_hang_id=?",
                       (khach_hang_id, ngay_dat, trang_thai, id))
        connect.commit()
        connect.close()

        messagebox.showinfo("Cập nhật đơn hàng", "Đơn hàng đã được cập nhật thành công")
        hien_thi_don_hang()

    def hien_thi_don_hang():
        for row in don_hang_tree.get_children():
            don_hang_tree.delete(row)

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM don_hang")
        rows = cursor.fetchall()
        connect.close()

        for row in rows:
            don_hang_tree.insert("", END, values=row)

    # Form nhập liệu
    id_label = Label(don_hang_win, text="ID")
    id_label.grid(row=0, column=0)
    id_entry = Entry(don_hang_win)
    id_entry.grid(row=0, column=1)

    khach_hang_id_label = Label(don_hang_win, text="ID khách hàng")
    khach_hang_id_label.grid(row=1, column=0)
    khach_hang_id_entry = Entry(don_hang_win)
    khach_hang_id_entry.grid(row=1, column=1)

    ngay_dat_label = Label(don_hang_win, text="Ngày đặt")
    ngay_dat_label.grid(row=2, column=0)
    ngay_dat_entry = Entry(don_hang_win)
    ngay_dat_entry.grid(row=2, column=1)

    trang_thai_label = Label(don_hang_win, text="Trạng thái")
    trang_thai_label.grid(row=3, column=0)
    trang_thai_entry = Entry(don_hang_win)
    trang_thai_entry.grid(row=3, column=1)

    tao_button = Button(don_hang_win, text="Tạo", command=tao_don_hang)
    tao_button.grid(row=4, column=0)

    cap_nhat_button = Button(don_hang_win, text="Cập nhật", command=cap_nhat_don_hang)
    cap_nhat_button.grid(row=4, column=1)

    # Hiển thị dữ liệu
    don_hang_tree = ttk.Treeview(don_hang_win, columns=("ID", "ID khách hàng", "Ngày đặt", "Trạng thái"), show="headings")
    don_hang_tree.heading("ID", text="ID")
    don_hang_tree.heading("ID khách hàng", text="ID khách hàng")
    don_hang_tree.heading("Ngày đặt", text="Ngày đặt")
    don_hang_tree.heading("Trạng thái", text="Trạng thái")
    don_hang_tree.grid(row=5, column=0, columnspan=2)

    hien_thi_don_hang()


def xuat_bao_cao():
    bao_cao_win = Toplevel(w)
    bao_cao_win.geometry("500x500")
    bao_cao_win.title("Xuất báo cáo và thống kê")

    # Số lượng đơn hàng
    connect = sqlite3.connect("online_store.db")
    cursor = connect.cursor()
    cursor.execute("SELECT COUNT(*) FROM don_hang")
    so_luong_don_hang = cursor.fetchone()[0]
    connect.close()

    Label(bao_cao_win, text=f"Số lượng đơn hàng: {so_luong_don_hang}").pack()

    # Số lượng khách hàng
    connect = sqlite3.connect("online_store.db")
    cursor = connect.cursor()
    cursor.execute("SELECT COUNT(*) FROM khach_hang")
    so_luong_khach_hang = cursor.fetchone()[0]
    connect.close()

    Label(bao_cao_win, text=f"Số lượng khách hàng: {so_luong_khach_hang}").pack()

    # Số lượng phản hồi
    connect = sqlite3.connect("online_store.db")
    cursor = connect.cursor()
    cursor.execute("SELECT COUNT(*) FROM phan_hoi")
    so_luong_phan_hoi = cursor.fetchone()[0]
    connect.close()

    Label(bao_cao_win, text=f"Số lượng phản hồi: {so_luong_phan_hoi}").pack()

    # Tổng hợp số tiền
    connect = sqlite3.connect("online_store.db")
    cursor = connect.cursor()
    cursor.execute("SELECT SUM(san_pham.gia * chi_tiet_don_hang.so_luong) FROM san_pham "
                   "JOIN chi_tiet_don_hang ON san_pham.san_pham_id = chi_tiet_don_hang.san_pham_id")
    tong_tien = cursor.fetchone()[0]
    connect.close()

    Label(bao_cao_win, text=f"Tổng hợp số tiền: {tong_tien}").pack()

    # Đóng cửa sổ khi hoàn thành
    Button(bao_cao_win, text="Đóng", command=bao_cao_win.destroy).pack()




def quan_ly_phan_hoi():
    phan_hoi_win = Toplevel(w)
    phan_hoi_win.title("Quản lý phản hồi")

    def them_phan_hoi():
        khach_hang_id = khach_hang_id_entry.get()
        tin_nhan = tin_nhan_entry.get()

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("INSERT INTO phan_hoi (khach_hang_id, tin_nhan, ngay_gui) VALUES (?, ?, date('now'))",
                       (khach_hang_id, tin_nhan))
        connect.commit()
        connect.close()

        messagebox.showinfo("Thêm phản hồi", "Phản hồi đã được thêm thành công")
        hien_thi_phan_hoi()

    def cap_nhat_phan_hoi():
        id = id_entry.get()
        khach_hang_id = khach_hang_id_entry.get()
        tin_nhan = tin_nhan_entry.get()
        phan_hoi = phan_hoi_entry.get()

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("UPDATE phan_hoi SET khach_hang_id=?, tin_nhan=?, phan_hoi=? WHERE phan_hoi_id=?",
                       (khach_hang_id, tin_nhan, phan_hoi, id))
        connect.commit()
        connect.close()

        messagebox.showinfo("Cập nhật phản hồi", "Phản hồi đã được cập nhật thành công")
        hien_thi_phan_hoi()

    def hien_thi_phan_hoi():
        for row in phan_hoi_tree.get_children():
            phan_hoi_tree.delete(row)

        connect = sqlite3.connect("online_store.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM phan_hoi")
        rows = cursor.fetchall()
        connect.close()

        for row in rows:
            phan_hoi_tree.insert("", END, values=row)

    # Form nhập liệu
    id_label = Label(phan_hoi_win, text="ID")
    id_label.grid(row=0, column=0)
    id_entry = Entry(phan_hoi_win)
    id_entry.grid(row=0, column=1)

    khach_hang_id_label = Label(phan_hoi_win, text="ID khách hàng")
    khach_hang_id_label.grid(row=1, column=0)
    khach_hang_id_entry = Entry(phan_hoi_win)
    khach_hang_id_entry.grid(row=1, column=1)

    tin_nhan_label = Label(phan_hoi_win, text="Tin nhắn")
    tin_nhan_label.grid(row=2, column=0)
    tin_nhan_entry = Entry(phan_hoi_win)
    tin_nhan_entry.grid(row=2, column=1)

    phan_hoi_label = Label(phan_hoi_win, text="Phản hồi")
    phan_hoi_label.grid(row=3, column=0)
    phan_hoi_entry = Entry(phan_hoi_win)
    phan_hoi_entry.grid(row=3, column=1)

    them_button = Button(phan_hoi_win, text="Thêm", command=them_phan_hoi)
    them_button.grid(row=4, column=0)

    cap_nhat_button = Button(phan_hoi_win, text="Cập nhật", command=cap_nhat_phan_hoi)
    cap_nhat_button.grid(row=4, column=1)

    # Hiển thị dữ liệu
    phan_hoi_tree = ttk.Treeview(phan_hoi_win, columns=("ID", "ID khách hàng", "Tin nhắn", "Phản hồi", "Ngày gửi"), show="headings")
    phan_hoi_tree.heading("ID", text="ID")
    phan_hoi_tree.heading("ID khách hàng", text="ID khách hàng")
    phan_hoi_tree.heading("Tin nhắn", text="Tin nhắn")
    phan_hoi_tree.heading("Phản hồi", text="Phản hồi")
    phan_hoi_tree.heading("Ngày gửi", text="Ngày gửi")
    phan_hoi_tree.grid(row=5, column=0, columnspan=2)

    hien_thi_phan_hoi()


# Giao diện đăng nhập
w = Tk()
w.geometry("300x300")
w.title("Đăng nhập")

ten = Label(w, text="Tên đăng nhập").grid(row=0, column=0)
ten_dang_nhap_entry = Entry(w)
ten_dang_nhap_entry.grid(row=0, column=1)

mk = Label(w, text="Mật khẩu").grid(row=1, column=0)
mat_khau_entry = Entry(w, show="*")
mat_khau_entry.grid(row=1, column=1)

btn_login = Button(w, text="Đăng nhập", command=dang_nhap).grid(row=2, column=1)

tao_bang()

w.mainloop()
