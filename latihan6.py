import sys

# Unpacking argv ke dalam variabel
script, nama, kota = sys.argv

# Ambil hobi dari input interaktif
hobi = input("Masukkan hobi kamu: ")

print("Nama File:", script)
print("Nama     :", nama)
print("Kota     :", kota)
print("Hobi kamu:", hobi)
