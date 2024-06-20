import tkinter as tk
from tkinter import messagebox
import random

w = tk.Tk()
w.geometry("400x400")
w.title("Bai Tap Buoi 17")

x = random.randint(1, 100)
count = 0

def kiem_tra_du_doan():
    global count
    try:
        du_doan = int(sodoan.get())
        count += 1

        if du_doan == x:
            messagebox.showinfo("Chuc mung", "Ban da doan dung so!")
            w.destroy()
        elif du_doan > x:
            messagebox.showinfo("Qua Cao", "So ban doan lon hon so can doan")
        else:
            messagebox.showinfo("Qua Thap", "So ban doan nho hon so can doan")

        if count >= 5 and du_doan != x:
            messagebox.showinfo("That bai", f"Ban da het luot doan. So bi mat la {x}.")
            w.destroy()
    except ValueError:
        messagebox.showerror("Du Lieu Khong Hop Le", "Vui long nhap mot so hop le.")

text = tk.Label(w, text="Nhap vao so ma ban doan")
text.pack(pady=5)

sodoan = tk.Entry(w)
sodoan.pack(pady=10)

nut_kiem_tra = tk.Button(w, text="Kiem Tra", command=kiem_tra_du_doan)
nut_kiem_tra.pack(pady=5)

w.mainloop()
