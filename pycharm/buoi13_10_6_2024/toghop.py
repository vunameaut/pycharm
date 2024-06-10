import sqlite3

with sqlite3.connect("it9.db") as conn:
    cursor = conn.cursor()

def cau1():
    cursor.execute(("""create table if not exists calls_name (
    id integer PRIMARY KEY ,
    first name text NOT NULL ,
    surname text NOT NULL,
    phone number NOT NULL
    );"""))

    conn.commit()

    cursor.execute(("""INSERT INTO calls_name 
                    (id, first, surname, phone) 
                    VALUES
    (1, 'John', 'Doe', '123-456-7890'),
    (2, 'Jane', 'Smith', '234-567-8901'),
    (3, 'Emily', 'Jones', '345-678-9012'),
    (4, 'Michael', 'Brown', '456-789-0123'),
    (5, 'Sarah', 'Davis', '567-890-1234');
    """))
    conn.commit()
def cau2():
    print("1. xem danh ba")
    print("2. them so dien thoai")
    print("3. tim kiem so dien thoai")
    print("4. xoa so dien thoai")
    print("5. thoat")
    chon = int(input("nhap vao lua chon cua ban: "))
    def viewphonebook():
        cursor.execute("SELECT * FROM calls_name")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    def addphone():
        id = int(input("Nhap vao id: "))
        ten = str(input("Nhap vao ten: "))
        ho = str(input("Nhap vao ho: "))
        so = int(input("Nhap vao so dien thoai: "))

        cursor.execute("""
            INSERT INTO calls_name (id, first,surname,phone)
            VALUES (?, ?, ?, ?)
            """, (id, ten, ho, so))

        conn.commit()

    def searchphonebook():
        ten = str(input("Nhap vao ten muon tim: "))
        cursor.execute("SELECT * FROM calls_name WHERE first = ?", (ten,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    def deletephonebook():
        ten = str(input("nhap vao ten muon xoa: "))
        cursor.execute("DELETE FROM calls_name where first = ?", (ten,))
        conn.commit()


    while True:
        match(chon):
            case 1:
                viewphonebook()
                break
            case 2:
                addphone()
                break
            case 3:
                searchphonebook()
                break
            case 4:
                deletephonebook()
                break
            case 5:
                break
def cau3():

    cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
                Name TEXT,
                PlaceBirth TEXT);
                """)
    conn.commit()

    cursor.execute("INSERT INTO Authors(Name, PlaceBirth) VALUES ('Agatha Christie', 'Torquay')")
    cursor.execute("INSERT INTO Authors(Name, PlaceBirth) VALUES ('Cecelia Ahern', 'Dublin')")
    cursor.execute("INSERT INTO Authors(Name, PlaceBirth) VALUES ('J.K. Rowling', 'Bristol')")
    cursor.execute("INSERT INTO Authors(Name, PlaceBirth) VALUES ('Oscar Wilde', 'Dublin')")
    conn.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                Author TEXT NOT NULL,
                datePub Number NOT NULL);
                """)
    conn.commit()

    cursor.execute("""INSERT INTO Books(title, Author, datePub) 
                VALUES ('De Profundis', 'Oscar Wilde', '1905')""")
    cursor.execute("""INSERT INTO Books(title, Author, datePub) 
                VALUES ('Harry Potter and the chamber of secrets', 'J.K. Rowling', '1998')""")
    cursor.execute("""INSERT INTO Books(title, Author, datePub) 
                VALUES ('Harry Potter and the prioner of Askaban', 'J.K. Rowling', '1999')""")
    cursor.execute("""INSERT INTO Books(title, Author, datePub) 
                VALUES ('Lyreblrd', 'Cecelia Ahern', '2017')""")
    cursor.execute("""INSERT INTO Books(title, Author, datePub) 
                VALUES ('Munder on the Orlient Express', 'Agatha Christie', '1934')""")
    cursor.execute("""INSERT INTO Books(title, Author, datePub) 
                VALUES ('Perfect', 'Cecelia Ahern', '2017')""")
    cursor.execute("""INSERT INTO Books(title, Author, datePub) 
                VALUES ('The marble collector', 'Cecelia Ahern', '2016')""")
    cursor.execute("""INSERT INTO Books(title, Author, datePub) 
                VALUES ('The murder on the links', 'Agatha Christie', '1923')""")
    cursor.execute("""INSERT INTO Books(title, Author, datePub) 
                VALUES ('The pictuce of Dorian Gray', 'Oscar Wilde', '1890')""")
    cursor.execute("""INSERT INTO Books(title, Author, datePub) 
                VALUES ('The secret advenry', 'Agatha Christie', '1921')""")
    cursor.execute("""INSERT INTO Books(title, Author, datePub) 
                VALUES ('The seven dlals mystery', 'Agatha Christie', '1929')""")
    cursor.execute("""INSERT INTO Books(title, Author, datePub) 
                VALUES ('The year i met you', 'Cecelia Ahern', '2014')""")
    conn.commit()

def cau4():
    Torquay = str(input("Nhập vào quê: "))
    cursor.execute("""SELECT Books.title, Books.datePub, Authors.Name
                    FROM Authors
                    INNER JOIN Books ON Authors.Name = Books.Author
                    WHERE Authors.PlaceBirth = ?;""", (Torquay,))
    result = cursor.fetchall()

    for _ in result:
        print(_)
def cau5():
    nam = str(input("Nhập vào năm: "))
    cursor.execute("""SELECT Books.title,Books.datePub, Authors.Name
                        FROM Authors
                        INNER JOIN Books ON Authors.Name = Books.Author
                        WHERE Books.datePub > ?
                        ORDER BY Books.datePub;""", (nam,))

    result = cursor.fetchall()

    for _ in result:
        print(_)

cau5()
