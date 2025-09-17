# multiple contructor (Overloading)
# 1. Pakai paramter default

"""
class Mahasiswa:
    def __init__(self, nama=None, nim=None):
        # if not nim.startswith("A11"):
        #     raise ValueError("NIM harus diawali dengan A11")

        self.nama = nama if nama else "Anonim"
        self.nim = nim if nim else "Tidak ada"

    def info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}")


m1 = Mahasiswa("Tati", "A11.2025.001")
m1.info()

m2 = Mahasiswa("Budi", "A11.2025.002")
m3 = Mahasiswa("Siti", "A11.2025.003")
m2.info()
m3.info()

m4 = Mahasiswa()
m4.info()
"""


# 2. Pakai Class Method (Factory Contructor)
class Mahasiswa:
    def __init__(self, nama, nim):

        self.nama = nama
        self.nim = nim

    @classmethod
    def from_dict(cls, data):
        return cls(data["nama"], data["nim"])

    def info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}")


data = {"nama": "Siti", "nim": "A11.2025.001"}
m = Mahasiswa.from_dict(data)
m.info()
