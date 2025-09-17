class Orang:
    # class attribute (berlaku untuk semua object)
    spesies = "Homo sapiens"

    def __init__(self, nama=None):
        self.nama = nama

    # method instance (punya akses ke self/objek)
    def sapa(self, nama):
        print(f"Halo {nama}, saya {self.nama} dari spesies {Orang.spesies}")


# Membuat object dan menambahkan atribut instance
o = Orang()
o.nama = "Oded"  # atribut instance dibuat dinamis

o.sapa("Tati")
print(o.spesies)


class Kucing:
    def suara(self):
        print("Meong")


k = Kucing()
k.suara()


# Mahasiswa.__init__(m1, "Tati", "A11.2025.001")
