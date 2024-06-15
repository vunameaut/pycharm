import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)
mycursor = mydb.cursor()

def cau1():
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            country_id INT PRIMARY KEY,
            country_name VARCHAR(255),
            region_id INT
        )
    """)
    mydb.commit()

def cau2():
    id_que = int(input("Nhập id: "))
    name_que = input("Nhập tên quê: ")
    regionid_que = int(input("Nhập region: "))

    sql = "INSERT INTO countries (country_id, country_name, region_id) VALUES (%s, %s, %s)"
    vl = (id_que, name_que, regionid_que)
    mycursor.execute(sql, vl)
    mydb.commit()

def cau3():
    check = ["Italy", "India", "China"]

    id_que = int(input("Nhập id: "))
    name_que = input("Nhập tên quê: ")

    while name_que not in check:
        print("Tên quê không hợp lệ, vui lòng nhập lại")
        name_que = input("Nhập tên quê: ")

    regionid_que = int(input("Nhập region: "))

    sql = "INSERT INTO countries (country_id, country_name, region_id) VALUES (%s, %s, %s)"
    vl = (id_que, name_que, regionid_que)
    mycursor.execute(sql, vl)
    mydb.commit()

def cau4():
    sql_jobs = """
        CREATE TABLE IF NOT EXISTS jobs (
            job_id VARCHAR(10) NOT NULL PRIMARY KEY,
            job_title VARCHAR(35) NOT NULL,
            min_salary DECIMAL(6, 0),
            max_salary DECIMAL(6, 0)
        )
    """
    mycursor.execute(sql_jobs)

    sql_job_history = """
        CREATE TABLE IF NOT EXISTS job_history (
            employee_id INT NOT NULL UNIQUE,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            job_id VARCHAR(10) NOT NULL,
            department_id INT,
            CONSTRAINT fk_job_id FOREIGN KEY (job_id) REFERENCES jobs(job_id)
        )
    """
    mycursor.execute(sql_job_history)
    mydb.commit()

def ex1():
    id_que = int(input("Nhập id: "))
    name_que = input("Nhập tên quê: ")
    regionid_que = int(input("Nhập region: "))

    sql = "INSERT INTO countries (country_id, country_name, region_id) VALUES (%s, %s, %s)"
    vl = (id_que, name_que, regionid_que)
    mycursor.execute(sql, vl)
    mydb.commit()

def ex2():
    sql = "ALTER TABLE countries ADD row_new INT"
    mycursor.execute(sql)
    mydb.commit()

def ex3():
    sql = """
        INSERT INTO countries (country_id, country_name, region_id, row_new)
        VALUES (10, 'India', 1001, 3)
    """
    mycursor.execute(sql)
    mydb.commit()

def ex4_5():
    try:
        id_que = input("Nhập job_id: ")
        title_que = input("Nhập job_title: ")
        min_salary_que = float(input("Nhập min_salary: "))
        max_salary_que = float(input("Nhập max_salary: "))

        sql = "INSERT INTO jobs (job_id, job_title, min_salary, max_salary) VALUES (%s, %s, %s, %s)"
        vl = (id_que, title_que, min_salary_que, max_salary_que)
        mycursor.execute(sql, vl)
        mydb.commit()
        print("Thêm thành công")

    except mysql.connector.Error as err:
        print("Lỗi: ", err)
        print("Vui lòng không nhập trùng job_id")
