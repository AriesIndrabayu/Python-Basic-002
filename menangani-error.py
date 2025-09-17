# ValueError
try:
    int("Ocim")
except ValueError:
    print("ValueError: tidak bisa konversi ke int")

# FileNotFoundError
try:
    open("tidak_ada.txt")
except FileNotFoundError:
    print("FileNotFoundError: file tidak ditemukan")

# TypeError
try:
    print("Tati" + 5)  # type: ignore
except TypeError:
    print("TypeError: operasi tipe tidak cocok")

# KeyError
try:
    data = {"nama": "Teti"}
    print(data["umur"])
except KeyError:
    print("KeyError: kunci 'umur' tidak ada")

# IndexError
try:
    daftar = ["Oded", "Tutu"]
    print(daftar[5])
except IndexError:
    print("IndexError: index di luar jangkauan")
