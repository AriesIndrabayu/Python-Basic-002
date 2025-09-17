# Prosedural:
nama = "oded"
umur = 20


def sapa(nama, umur):
    print(f"Halo, nama saya {nama}, umur saya {umur} tahun.")


sapa(nama, umur)


# OOP:
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def sapa(self):
        print(f"Halo, nama saya {self.nama}, umur saya {self.umur} tahun.")


Orang1 = Orang("Tati", 23)
Orang1.sapa()
