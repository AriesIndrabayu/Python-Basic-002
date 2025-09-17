class Dosen:
    def __init__(self, nama):
        self.nama = nama

    def sapa(self):
        return f"Dosen {self.nama} menyapa."


class Staff:
    def __init__(self, nama):
        self.nama = nama

    def sapa(self):
        return f"Staff {self.nama} menyapa."


def sapaan_massal(objek_list):
    for o in objek_list:
        # polymorphism: cukup panggil .sapa() apapun tipenya
        print(o.sapa())


daftar = [Dosen("Oded"), Staff("Teti"), Dosen("Ocah")]
sapaan_massal(daftar)
