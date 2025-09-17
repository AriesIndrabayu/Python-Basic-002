"""
# Kombinasi Variabel
nama = "Titin"
umur = 20
print(nama, "berumur", umur, "tahun")

# contoh lain:
panjang = 5
lebar = 3
luas = panjang * lebar
print("Luas persegi panjang:", luas)

# contoh f-string
nama = "Dudung"
pekerjaan = "Kasir"
gaji = 2000000
tunjangan = 10000
total = gaji + tunjangan
nilai1 = "10000"
nilai2 = 1000


print(f"{nama} bekerja sebagai {pekerjaan} dengan gaji Rp. {total:,}.")

print("%s bekarja sebagai %s dengan gaji Rp. %d" % (nama, pekerjaan, gaji))

# Format angka sebagai uang:
gaji = 2000000
print(f"Gaji: {gaji:,}")

# format Desimal
pi = 3.1415926535
print(f"pi: {pi:.2f}")
print(f"pi: {pi:.4f}")

# format Persen
persentase = 0.876
print(f"Tingkat keberhasilan: {persentase:.2%}")

# format Tanggal
from datetime import datetime

hari_ini = datetime.now()
print(f"Tanggal Sekarang: {hari_ini: %d-%m-%Y}")
print(f"Hari Ini: {hari_ini: %A, %d %B %Y}")

# format lebar kolom
nama = "Bayu"
print(f"{nama:>10}")
print(f"{nama:<10}")
print(f"{nama:^10}")
"""

# implementasi dalam bentuk tabel
nama1 = "Andi"
usia1 = 21
kota1 = "Jakarta"

nama2 = "Budi"
usia2 = 22
kota2 = "Makasar"

# Tabel dengan lebar kolom rata kiri-kanan
print(f"{'Nama':<10} {'Umur':^6} {"Kota":<10}")
print("-" * 28)
print(f"{nama1:<10} {usia1:^6} {kota1:>10}")
print(f"{nama2:<10} {usia2:^6} {kota2:>10}")
