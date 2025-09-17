# 1. fungsi pembagian yang aman
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Pembagi tidak boleh nol.")
        return None


print(safe_divide(10, 2))
print(safe_divide(10, 0))


# 2. fungsi parse int list
def parse_int_list(lst):
    hasil = []
    for s in lst:
        try:
            hasil.append(int(s))
        except ValueError:
            print(f"Lewati: '{s}' bukan angka")
    return hasil


print(parse_int_list(["10", "Tati", "25", "Ocah", "7"]))


# 3. Baca file dengan aman
def baca_file(nama_file):
    try:
        with open(nama_file, "r") as f:
            isi = f.read()
            print("=== Isi File ===")
            print(isi[:12] + ("..." if len(isi) > 12 else ""))
    except FileNotFoundError:
        print("FileNotFoundError: file tidak ditemukan")
    finally:
        print("Selesai membaca")


baca_file("tidak_ada.txt")
baca_file("backup.txt")


# 4. Ambil data dari fungsi dict ambil umur
def ambil_umur_orang(orang):
    try:
        return orang["umur"]
    except KeyError:
        print("Umur tidak tersedia")
        return -1


print(ambil_umur_orang({"nama": "Udung", "umur": 27}))
print(ambil_umur_orang({"nama": "Ujang"}))


# 5. Fungsi validasi
def ambil_nilai(angka):
    n = int(angka)  # bisa ValueError
    if n < 0:
        raise ValueError("Nilai tidak boleh negatif")
    return n


try:
    print(ambil_nilai("15"))
    # print(ambil_nilai("-13"))
    print(ambil_nilai("Ujang"))
except ValueError as e:
    print("Error:", type(e).__name__, "-", e)


# 6. try-except-else-finally
def proses(a, b):
    try:
        x, y = int(a), int(b)
        hasil = x / y
    except ValueError:
        print("Input harus angka.")
    except ZeroDivisionError:
        print("Tidak boleh bagi nol.")
    else:
        print("Hasil:", hasil)
    finally:
        print("Selesai blok")


proses("10", "2")
proses("Titi", "2")
proses("10", "0")
