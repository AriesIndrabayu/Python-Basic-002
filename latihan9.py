# fungsi dengan parameter default
def diskon(harga, potongan=10):
    total = harga - (harga * potongan / 100)
    print(f"Harga setelah diskon {potongan}%: {total}")


diskon(100000)
diskon(100000, 20)


# Fungsi dengan positional & keyword argument
def profil(nama, umur, kota):
    print(f"Nama: {nama}, Umur: {umur}, Kota: {kota}")


profil("Teti", 30, "Jakarta")  # positional
profil(kota="Bandung", nama="Tati", umur=25)


# Fungsi dengan *args
def hitung_total(*args):
    total = sum(args)
    print(f"Total: {total}")


hitung_total(10, 20, 30)
hitung_total(5, 15, 25, 35, 45)


# Fungsi dengan **kwargs
def cetak_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


cetak_info(nama="Oded", hobi="Ngoding")


# Fungsi sebagai parameter
def jalankan_fungsi(func, *args):
    return func(*args)


def kali(a, b):
    return a * b


hasil = jalankan_fungsi(kali, 5, 4)
print("Hasil:", hasil)


# Fungsi Rekursif
def buat_pengali(n):
    def pengali(x):
        return x * n

    return pengali


kali_3 = buat_pengali(3)
print(kali_3(10))


def hitung_mundur(n):
    if n <= 0:
        print("Selesai!")
    else:
        print(n)
        hitung_mundur(n - 1)


hitung_mundur(5)

# Lamda
kuadrat = lambda x: x * x
print(kuadrat(5))

"""
variabel = lamda arg1, arg2, ...: expression
# versi fungsi biasa
def square(x):
    return x * x


# versi lamda
square = lambda x: x * x
print(square(5))
"""

# lamda dengan *args
f3 = lambda *args: sum(args)
print(f3(1, 2, 3, 4))
# lamda dengan **kwargs
f4 = lambda **kwargs: list(kwargs.keys())
print(f4(a=1, b=2))
