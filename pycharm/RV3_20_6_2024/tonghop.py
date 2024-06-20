from tkinter import *
from tkinter import messagebox, simpledialog, ttk

import mysql.connector

def taodatabase():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS library")
    print("ket noi thanh cong")

def taobang():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="library"
    )
    mycursor = mydb.cursor()


    mycursor.execute("CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), publication_year INT, available BOOLEAN)")


    mycursor.execute("CREATE TABLE IF NOT EXISTS borrowings (id INT AUTO_INCREMENT PRIMARY KEY, book_id INT, user_name VARCHAR(255), borrow_date DATE, return_date DATE, FOREIGN KEY (book_id) REFERENCES books(id))")




    data_sach = [
        ("Book 1", "Author 1", 2020, True),
        ("Book 2", "Author 2", 2019, False),
        ("Book 3", "Author 3", 2021, True),
        ("Book 4", "Author 4", 2018, False),
        ("Book 5", "Author 5", 2022, True),
        ("Book 6", "Author 6", 2017, False),
        ("Book 7", "Author 7", 2023, True),
        ("Book 8", "Author 8", 2016, False),
        ("Book 9", "Author 9", 2024, True),
        ("Book 10", "Author 10", 2015, False)
    ]

    query = "INSERT INTO books (title, author, publication_year, available) VALUES (%s, %s, %s, %s)"
    mycursor.executemany(query, data_sach)
    mydb.commit()


    data_tacgia = [
        (1, "User 1", "2022-01-01", "2022-01-15"),
        (2, "User 2", "2022-02-01", "2022-02-15"),
        (3, "User 3", "2022-03-01", "2022-03-15"),
        (4, "User 4", "2022-04-01", "2022-04-15"),
        (5, "User 5", "2022-05-01", "2022-05-15"),
        (6, "User 6", "2022-06-01", "2022-06-15"),
        (7, "User 7", "2022-07-01", "2022-07-15"),
        (8, "User 8", "2022-08-01", "2022-08-15"),
        (9, "User 9", "2022-09-01", "2022-09-15"),
        (10, "User 10", "2022-10-01", "2022-10-15")
    ]

    query = "INSERT INTO borrowings (book_id, user_name, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
    mycursor.executemany(query, data_tacgia)
    mydb.commit()






def quan_ly_sach():
    w.withdraw()
    sub_window = Toplevel()
    sub_window.title("Quản lý sách")
    sub_window.attributes('-fullscreen', True)

    def on_close():
        w.deiconify()
        sub_window.destroy()

    sub_window.protocol("WM_DELETE_WINDOW", on_close)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="library"
    )
    mycursor = mydb.cursor()

    def hien_thi_danh_sach_sach():
        mycursor.execute("SELECT * FROM books")
        books = mycursor.fetchall()

        for i in viewtree.get_children():
            viewtree.delete(i)

        if books:
            for book in books:
                viewtree.insert('', 'end', values=(book[0], book[1], book[2], book[3], 'Có' if book[4] else 'Không'))

    def them_sach():
        title = title_entry.get()
        author = author_entry.get()
        publication_year = year_entry.get()
        available = available_var.get()

        if title and author and publication_year:
            query = "INSERT INTO books (title, author, publication_year, available) VALUES (%s, %s, %s, %s)"
            values = (title, author, publication_year, available)
            mycursor.execute(query, values)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Thêm sách thành công")
            hien_thi_danh_sach_sach()
        else:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin sách")

    def cap_nhat_sach():
        book_id = simpledialog.askinteger("Nhập", "Nhập ID sách cần cập nhật")
        title = title_entry.get()
        author = author_entry.get()
        publication_year = year_entry.get()
        available = available_var.get()

        if book_id and title and author and publication_year:
            query = "UPDATE books SET title=%s, author=%s, publication_year=%s, available=%s WHERE id=%s"
            values = (title, author, publication_year, available, book_id)
            mycursor.execute(query, values)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Cập nhật sách thành công")
            hien_thi_danh_sach_sach()
        else:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin sách")

    def xoa_sach():
        book_id = simpledialog.askinteger("Nhập", "Nhập ID sách cần xóa")

        if book_id:
            query = "DELETE FROM books WHERE id=%s"
            mycursor.execute(query, (book_id,))
            mydb.commit()
            messagebox.showinfo("Thông báo", "Xóa sách thành công")
            hien_thi_danh_sach_sach()
        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập ID sách hợp lệ")

    def tim_kiem_sach():
        title = title_entry.get()

        if title:
            query = "SELECT * FROM books WHERE title LIKE %s"
            mycursor.execute(query, (f"%{title}%",))
            results = mycursor.fetchall()

            for i in viewtree.get_children():
                viewtree.delete(i)

            if results:
                for row in results:
                    viewtree.insert('', 'end', values=(row[0], row[1], row[2], row[3], 'Có' if row[4] else 'Không'))
            else:
                messagebox.showinfo("Thông tin", "Không tìm thấy sách")

    columns = ('ID', 'Tên sách', 'Tác giả', 'Năm xuất bản', 'Có sẵn')
    viewtree = ttk.Treeview(sub_window, columns=columns, show='headings', selectmode='browse')
    viewtree.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    for col in columns:
        viewtree.heading(col, text=col)

    Label(sub_window, text="Tên sách").grid(row=1, column=0, padx=10, pady=10)
    title_entry = Entry(sub_window)
    title_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(sub_window, text="Tác giả").grid(row=2, column=0, padx=10, pady=10)
    author_entry = Entry(sub_window)
    author_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(sub_window, text="Năm xuất bản").grid(row=3, column=0, padx=10, pady=10)
    year_entry = Entry(sub_window)
    year_entry.grid(row=3, column=1, padx=10, pady=10)

    Label(sub_window, text="Có sẵn").grid(row=4, column=0, padx=10, pady=10)
    available_var = BooleanVar()
    Checkbutton(sub_window, text="Có sẵn", variable=available_var).grid(row=4, column=1, padx=10, pady=10)

    Button(sub_window, text="Thêm sách", command=them_sach).grid(row=5, column=0, padx=10, pady=10)
    Button(sub_window, text="Cập nhật sách", command=cap_nhat_sach).grid(row=5, column=1, padx=10, pady=10)
    Button(sub_window, text="Xóa sách", command=xoa_sach).grid(row=6, column=0, padx=10, pady=10)
    Button(sub_window, text="Tìm kiếm sách", command=tim_kiem_sach).grid(row=6, column=1, padx=10, pady=10)
    Button(sub_window, text="Quay lại", command= on_close).grid(row=7, column=1, padx=10, pady=10)

    hien_thi_danh_sach_sach()
    sub_window.mainloop()


def muonsach():
    w.withdraw()
    sub_window = Toplevel()
    sub_window.title("Mượn sách")
    sub_window.attributes('-fullscreen', True)

    def on_close():
        w.deiconify()
        sub_window.destroy()

    sub_window.protocol("WM_DELETE_WINDOW", on_close)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="library"
    )
    mycursor = mydb.cursor()

    def hien_thi_danh_sach_sach_muon():
        mycursor.execute("SELECT borrowings.id, books.title, books.author, borrowings.borrow_date, borrowings.return_date FROM borrowings INNER JOIN books ON borrowings.book_id = books.id")
        borrowed_books = mycursor.fetchall()

        for i in viewtree.get_children():
            viewtree.delete(i)

        if borrowed_books:
            for book in borrowed_books:
                viewtree.insert('', 'end', values=(book[0], book[1], book[2], book[3], book[4]))
        else:
            messagebox.showinfo("Thông tin", "Không có sách nào được mượn")

    def muon_sach():
        book_id = simpledialog.askinteger("Nhập", "Nhập ID sách cần mượn")
        user_name = user_entry.get()
        borrow_date = borrow_date_entry.get()
        return_date = return_date_entry.get()

        if book_id and user_name and borrow_date and return_date:
            query = "INSERT INTO borrowings (book_id, user_name, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
            values = (book_id, user_name, borrow_date, return_date)
            mycursor.execute(query, values)
            mydb.commit()
            messagebox.showinfo("Thông báo", "Mượn sách thành công")
            hien_thi_danh_sach_sach_muon()
        else:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin sách và ngày mượn/trả")

    def tra_sach():
        borrowing_id = simpledialog.askinteger("Nhập", "Nhập ID mượn sách cần trả")

        if borrowing_id:
            query = "DELETE FROM borrowings WHERE id=%s"
            mycursor.execute(query, (borrowing_id,))
            mydb.commit()
            messagebox.showinfo("Thông báo", "Trả sách thành công")
            hien_thi_danh_sach_sach_muon()
        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập ID mượn sách hợp lệ")

    columns = ('ID', 'Tên sách', 'Tác giả', 'Ngày mượn', 'Ngày trả')
    viewtree = ttk.Treeview(sub_window, columns=columns, show='headings', selectmode='browse')
    viewtree.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    for col in columns:
        viewtree.heading(col, text=col)

    Label(sub_window, text="Tên người mượn").grid(row=1, column=0, padx=10, pady=10)
    user_entry = Entry(sub_window)
    user_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(sub_window, text="Ngày mượn").grid(row=2, column=0, padx=10, pady=10)
    borrow_date_entry = Entry(sub_window)
    borrow_date_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(sub_window, text="Ngày trả").grid(row=3, column=0, padx=10, pady=10)
    return_date_entry = Entry(sub_window)
    return_date_entry.grid(row=3, column=1, padx=10, pady=10)

    Button(sub_window, text="Mượn sách", command=muon_sach).grid(row=4, column=0, padx=10, pady=10)
    Button(sub_window, text="Trả sách", command=tra_sach).grid(row=4, column=1, padx=10, pady=10)
    Button(sub_window, text="Quay lại", command= on_close).grid(row=5, column=1, padx=10, pady=10)

    hien_thi_danh_sach_sach_muon()
    sub_window.mainloop()
def xemthongtin():
    w.withdraw()
    sub_window = Toplevel()
    sub_window.title("Xem thông tin sách đã mượn")
    sub_window.attributes('-fullscreen', True)

    def on_close():
        w.deiconify()
        sub_window.destroy()

    sub_window.protocol("WM_DELETE_WINDOW", on_close)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="library"
    )
    mycursor = mydb.cursor()

    def hien_thi_danh_sach_sach_muon():
        mycursor.execute("SELECT borrowings.id, books.title, books.author, borrowings.borrow_date, borrowings.return_date FROM borrowings INNER JOIN books ON borrowings.book_id = books.id")
        borrowed_books = mycursor.fetchall()

        for i in viewtree.get_children():
            viewtree.delete(i)

        if borrowed_books:
            for book in borrowed_books:
                viewtree.insert('', 'end', values=book)

    columns = ('ID', 'Tên sách', 'Tác giả', 'Ngày mượn', 'Ngày trả')
    viewtree = ttk.Treeview(sub_window, columns=columns, show='headings', selectmode='browse')
    viewtree.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    for col in columns:
        viewtree.heading(col, text=col)

    Button(sub_window, text="Quay lại", command=on_close).grid(row=1, column=0, padx=10, pady=10)

    hien_thi_danh_sach_sach_muon()
    sub_window.mainloop()
def sach_dang_muon():
    w.withdraw()
    sub_window = Toplevel()
    sub_window.title("Sách đang được mượn")
    sub_window.attributes('-fullscreen', True)

    def on_close():
        w.deiconify()
        sub_window.destroy()

    sub_window.protocol("WM_DELETE_WINDOW", on_close)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="library"
    )
    mycursor = mydb.cursor()

    def hien_thi_danh_sach_sach_muon():
        mycursor.execute("SELECT books.title, books.author, borrowings.borrow_date, borrowings.return_date FROM borrowings INNER JOIN books ON borrowings.book_id = books.id")
        borrowed_books = mycursor.fetchall()

        for i in viewtree.get_children():
            viewtree.delete(i)

        if borrowed_books:
            for book in borrowed_books:
                viewtree.insert("", "end", values=book)

    columns = ('Tên sách', 'Tác giả', 'Ngày mượn', 'Ngày trả')
    viewtree = ttk.Treeview(sub_window, columns=columns, show='headings', selectmode='browse')
    viewtree.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    for col in columns:
        viewtree.heading(col, text=col)

    Button(sub_window, text="Quay lại", command=on_close).grid(row=1, column=0, padx=10, pady=10)

    hien_thi_danh_sach_sach_muon()
    sub_window.mainloop()
def kiemtra():
    w.withdraw()
    sub_window = Toplevel()
    sub_window.title("Kiểm tra")
    sub_window.attributes('-fullscreen', True)

    def on_close():
        w.deiconify()
        sub_window.destroy()

    sub_window.protocol("WM_DELETE_WINDOW", on_close)

    def check_book_availability():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="library"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM books WHERE available = True")
        available_books = mycursor.fetchall()
        mydb.close()

        for book in available_books:
            tree.insert('', 'end', values=book)

    columns = ('ID', 'Title', 'Author', 'Available')
    tree = ttk.Treeview(sub_window, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)

    tree.pack(fill=BOTH, expand=True)

    Button(sub_window, text="Kiểm tra sách còn tồn", command=check_book_availability).pack(pady=20)
    Button(sub_window, text="Quay lại", command=on_close).pack(pady=20)

    sub_window.mainloop()

def formql():
    w.withdraw()
    sub_window = Toplevel()
    sub_window.title("Yêu cầu người dùng")
    sub_window.attributes('-fullscreen', True)

    def on_close():
        w.deiconify()
        sub_window.destroy()

    sub_window.protocol("WM_DELETE_WINDOW", on_close)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="library"
    )
    mycursor = mydb.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_requests (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        request TEXT NOT NULL
    );
    """
    mycursor.execute(create_table_query)

    def save_user_request():
        name = name_entry.get()
        email = email_entry.get()
        request = request_text.get("1.0", "end-1c")

        insert_request_query = "INSERT INTO user_requests (name, email, request) VALUES (%s, %s, %s)"
        request_data = (name, email, request)
        mycursor.execute(insert_request_query, request_data)
        mydb.commit()
        mydb.close()

        messagebox.showinfo("Success", "Yêu cầu của bạn đã được gửi thành công!")

    Label(sub_window, text="Họ và tên").grid(row=0, column=0, padx=10, pady=10)
    name_entry = Entry(sub_window)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(sub_window, text="Email").grid(row=1, column=0, padx=10, pady=10)
    email_entry = Entry(sub_window)
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(sub_window, text="Yêu cầu").grid(row=2, column=0, padx=10, pady=10)
    request_text = Text(sub_window, height=10, width=50)
    request_text.grid(row=2, column=1, padx=10, pady=10)

    Button(sub_window, text="Gửi yêu cầu", command=save_user_request).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    Button(sub_window, text="Quay lại", command=on_close).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    sub_window.mainloop()
w = Tk()
w.title("Library Management System")
w.geometry("800x600")
w.attributes('-fullscreen', True)

# Tạo các nút và gán hàm tương ứng
button1 = Button(w, text="1. Thêm, Cập nhật, Xóa, Tìm kiếm sách", command=quan_ly_sach)
button2 = Button(w, text="2. Mượn và Trả sách", command=muonsach)
button3 = Button(w, text="3. Xem thông tin sách đã mượn", command=xemthongtin)
button4 = Button(w, text="4. Xem danh sách sách đang được mượn", command=sach_dang_muon)
button5 = Button(w, text="5. Kiểm tra danh sách tồn tại", command=kiemtra)
button6 = Button(w, text="6. Tạo yêu cầu người dùng", command=formql)
button7 = Button(w, text="7. Đóng chương trình", command=exit)

# Đặt các nút vào cửa sổ
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)
button5.pack(pady=10)
button6.pack(pady=10)
button7.pack(pady=10)

taodatabase()
taobang()
w.mainloop()



























