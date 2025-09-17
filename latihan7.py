"""
# Membuka file bernama 'data.txt' dalam mode baca (read only)
# Buka File
file = open("data.txt", "r", encoding="cp1252")

# Ambil/Baca isi file
isi = file.read()

# Tampilkan
print(isi)

# Tutup kembali filenya
file.close()


# with open("data.txt", "r", encoding="cp1252") as f:
#     isi = f.read()
#     print(isi)
"""

"""
Membuka dan Membaca File
from sys import argv

script, nama_file = argv
file = open(nama_file, "r")
print(f"Isi dari {nama_file}:\n{file.read()}")
file.close()
"""

"""
# Membuka dan menulis File
from sys import argv

script, nama_file = argv
file = open(nama_file, "w")
file.write(
    "Halo, ini teks baru!\nSaya sedang mencoba buka dan menulis file teks dengan python."
)
# print(f"Isi dari {nama_file}:\n{file.read()}")
file.close()

# Membuka dan menambahkan data baru ke file tanpa menghapus data lama

from sys import argv

script, nama_file = argv
file = open(nama_file, "a")
file.write("\nOcim bergabung di kelas.\n")
file.close()

# Membaca file dalam mode binary
with open("logo.png", "rb") as file:
    data = file.read(20)
    print(data)
"""

# Membaca file dan menulis file dalam bentuk biner
with open("python.png", "rb") as file:
    data = file.read()
    # print(data)

with open("logo_copy.png", "wb") as file_salinan:
    file_salinan.write(data)

print("File berhasil disalin")
