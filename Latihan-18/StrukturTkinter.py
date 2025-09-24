import tkinter as tk

window = tk.Tk()
window.title("Halo GUI Python")
window.geometry("300x200")  # lebar x tinggi
window.resizable(False, False)

label1 = tk.Label(window, text="Angka pertama:")
label1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(window, text="Angka kedua:")
label2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=5, pady=5)


def tambah():
    a = float(entry1.get())
    b = float(entry2.get())
    hasil.config(text=f"Hasil: {a+b}")


def kurang():
    a = float(entry1.get())
    b = float(entry2.get())
    hasil.config(text=f"Hasil: {a-b}")


def kali():
    a = float(entry1.get())
    b = float(entry2.get())
    hasil.config(text=f"Hasil: {a*b}")


def bagi():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        hasil.config(text=f"Hasil: {a/b}")
    except ZeroDivisionError:
        hasil.config(text="Error: Tidak bisa dibagi nol!")


hasil = tk.Label(window, text="Hasil: -", font=("Arial", 12))
hasil.grid(row=3, column=0, columnspan=2, pady=10)


# ==== Frame Tombol ====
frame_btn = tk.Frame(window)
frame_btn.grid(row=2, column=0, columnspan=2, pady=10)


btn_tambah = tk.Button(frame_btn, text="+", width=5, command=tambah)
btn_tambah.grid(row=2, column=0, padx=5)
btn_kurang = tk.Button(frame_btn, text="-", width=5, command=kurang)
btn_kurang.grid(row=2, column=1, padx=5)
btn_kali = tk.Button(frame_btn, text="x", width=5, command=kali)
btn_kali.grid(row=2, column=2, padx=5)
btn_bagi = tk.Button(frame_btn, text=":", width=5, command=bagi)
btn_bagi.grid(row=2, column=3, padx=5)

window.mainloop()
