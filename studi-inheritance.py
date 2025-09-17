"""
analogi:
parent = "template dasar"
child = "versi khusus" dari parent, yangbisa:
        - langsung pakai fitur dari parent atau
        - menambahkan/menyesuaikan(override) sesuai kebutuhan
"""


class Orang:  # Parent class
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print(f"{self.nama}, {self.umur} tahun")


class Mahasiswa(Orang):  # Child class
    def __init__(self, nama, umur, nim):
        # panggil constructor parent
        # MRO ==> Method Resolution Order [Mahasiswa, Orang, object]
        super().__init__(nama, umur)
        self.nim = nim

    # override method
    def info(self):
        print(f"{self.nama}, {self.umur} tahun, NIM: {self.nim}")


m = Mahasiswa("Tuti", 21, "A11.2025.007")
m.info()

"""
konsep penting:
1. sintaks pewarisan
2. super() ==> digunakan untuk memanggil method milik parent class.
3. Method Overriding
4. Override dengan Tambahan ==> pakai method parent + menambahkan fitur baru

Bentuk Inheritance:
1. Single Inheritance => 1 parent, 1 child
2. Multilevel Inheritance ==> Perawisan bertingkat
3. Multiple Inheritance ==> Satu Child dari beberapa parent
    class A: ...
    class B: ...
    class C(A, B): ....

"""
