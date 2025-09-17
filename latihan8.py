"""
# Tanpa Parameter
def ucapan():
    print("Belajar Python itu menyenangkan!")


print("Mulai program")
ucapan()
print("Program selesai")


# dengan parameter
def sapa_nama(nama):
    print(f"Halo {nama}, selamat belajar python!")


sapa_nama("Oded")
sapa_nama("Tati")

# dengan Banyak paramter
def biodata(nama, umur):
    print(f"Nama:   {nama}")
    print(f"Umur:   {umur} tahun")


biodata("Udung", 25)
biodata("Tuti", 30)
# fungsi dummy
def fitur_baru():
    pass  # artinya belum ada perintah


fitur_baru()
nama = "Ocah"  # variabel global


def buat_nama():
    nama = "Ujang"  # variabel lokal
    print(f"Nama di dalam fungsi: {nama}")


buat_nama()
print(nama)
def luas_persegi(sisi):
    return sisi * sisi


hasil = luas_persegi(5)
print(f"Luas persegi: {hasil}")

# Fungsi membaca seluruh file
def baca_file(nama_file):
    with open(nama_file, "r") as file:
        print(file.read())


# Fungsi "Kursor ke Awal"
def baca_ulang(nama_file):
    with open(nama_file, "r") as file:
        print(file.readline())
        file.seek(0)  # kembali ke awal dokumen
        print(file.readline())


# Fungsi untuk membaca per baris
def baca_per_baris(nama_file):
    with open(nama_file, "r") as file:
        no = 1
        for baris in file:
            print(f"{no}. {baris.strip()} {len(baris.strip())}")
            no = no + 1


# Fungsi mengubah data per baris
def ubah_baris(nama_file, baris_ke, teks_baru):
    with open(nama_file, "r") as file:
        data = file.readlines()
    data[baris_ke - 1] = teks_baru + "\n"
    with open(nama_file, "w") as file:
        file.writelines(data)


# Fungsi untuk menghapus per baris
def hapus_baris(nama_file, baris_ke):
    with open(nama_file, "r") as file:
        data = file.readlines()
    data.pop(baris_ke - 1)
    with open(nama_file, "w") as file:
        file.writelines(data)


hapus_baris("data.txt", 2)
def sapa_semua(daftar_nama):
    for nama in daftar_nama:
        print(f"Halo {nama}, selamat belajar python!")


sapa_semua(["Oded", "Tati", "Tuti"])
"""


def ganti_kata(nama_file, kata_lama, kata_baru):
    with open(nama_file, "r") as file:
        teks = file.read()
    teks = teks.replace(kata_lama, kata_baru)
    with open(nama_file, "w") as file:
        file.write(teks)


ganti_kata("data.txt", "Ujang", "Yayan")
