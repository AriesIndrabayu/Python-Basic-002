# Praktek ke-1:
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul  # atribut judul
        self.penulis = penulis  # atribut penulis

    def info(self):
        print(f"'{self.judul}' oleh {self.penulis}")


b = Buku("Pemograman Python Dasar", "Tati")
b.info()


# Praktek ke-2:
class Suhu:
    def __init__(self, celcius=0.0):
        self.__celcius = 0.0
        self.celcius = celcius

    @property
    def celcius(self):
        return self.__celcius

    @celcius.setter
    def celcius(self, val):
        if val < -273.15:
            print(f"Tidak valid: dibawah nol mutlak.")
            return
        self.__celcius = val


s = Suhu()
s.celcius = -300
s.celcius = 25.5
print(s.celcius)


# Praktek ke-3:
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def info(self):
        print(f"{self.nama} bergaji {self.gaji}")


class Manager(Karyawan):
    def __init__(self, nama, gaji, bonus):
        super().__init__(nama, gaji)
        self.bonus = bonus

    def info(self):
        total = self.gaji + self.bonus
        print(f"{self.nama} (Manager), total gaji: {total}")


m = Manager("Ujang", 7_000_000, 3_000_000)
m.info()


# Praktek ke-4:
def cetak_info(obj):
    obj.info()


b = Buku("Algoritma", "Oded")
k = Karyawan("Titi", 5_500_000)
m = Manager("Teti", 8_000_000, 2_000_000)

# looping dengan polymorphism
for o in [b, k, m]:
    cetak_info(o)


# Praktek ke-5:
class Keranjang:
    def __init__(self):
        self.__items = []  # private-like

    def tambah(self, item):
        self.__items.append(item)

    def hapus(self, item):
        if item in self.__items:
            self.__items.remove(item)

    def daftar(self):
        return list(self.__items)


k = Keranjang()
k.tambah("Apel")
k.tambah("Jeruk")
k.hapus("Salak")
print(k.daftar())


# Praktek ke-6:
class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def rata2(self):
        return sum(self.nilai) / len(self.nilai)


m = Mahasiswa("Ocim", [80, 90, 85])
print(m.rata2())


# Praktek ke-7:
class Kucing:
    def bersuara(self):
        return "Meong"


class Anjing:
    def bersuara(self):
        return "Guk"


def uji_suara(daftar):
    for h in daftar:
        print(h.bersuara())


uji_suara([Kucing(), Anjing(), Kucing()])
