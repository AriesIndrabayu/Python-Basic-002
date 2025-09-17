"""
# 1. Escape Characters
print("Halo, nama saya Oded\nUmur saya 20 tahun")
print("Harga barang:\tRp 15,000")
print("Ini tanda backslash: \\")
print('Dia berkata: "Python itu keren!"')


# 2. input()
nama = input("Nama:")
umur = input("Umur:")
print(f"Nama:\t{nama}\nUmur:\t{umur} tahun")

# 3. prompt
prompt = "> "
print("Masukan nama Anda:")
nama = input(prompt)
print("Masukan umur Anda:")
umur = input(prompt)

print(f"Halo {nama}, umurmu {umur} tahun")
# 4. Prompt didalam input()
prompt = "\n> "
nama = input(f"Masukan nama: {prompt}")
print(f"Halo {nama}!")
# 5 Gabungan teks + Prompt
prompt = "Halo! Masukkan nama Anda: "
prompt += "\n(Tekan Enter jika ingin keluar)\n> "
nama = input(prompt)
print(f"Selamat datang, {nama}")
"""

# Soal 1
nama = input("Masukkan nama: ")
hobi = input("Masukkan hobi: ")
print(f"Nama: {nama}\nHobi: {hobi}")

# Soal 2
print('Dia berkata: "Saya suka Python"')

# Soal 3
harga = input("Masukkan harga: ")
print(f"Harga Barang:\tRp {int(harga)}")

# soal 4
prompt = "\n> "
nama = input(f"Siapa namamu?{prompt}")
usia = input(f"Berapa usiamu?{prompt}")
print(f"Halo {nama}, usiamu sekarang {usia} tahun")
