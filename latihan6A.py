import sys

# Unpacking ARGV
namaFile, nama, umur = sys.argv

# Ambil hobi lewat input
hobi = input("Masukkan hobi kamu: ")

# Tampilkan hasilnya
print("\n--- PROFIL ---")
print(f"Nama   : {nama}")
print(f"Umur   : {umur} Tahun")
print(f"Hobi   : {hobi}")
