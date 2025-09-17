"""
encapsulation = "membungkus sesuatu"
tujuan:
1. melindungi data
2. memberi kontrol
3. membuat kode lebih rapi & terstruktur
4. mengurangi bug
"""


class AkunBank:
    def __init__(self, pemilik, saldo_awal=0):
        self.pemilik = pemilik  # public
        self.__saldo = saldo_awal  # private-like

    @property
    def saldo(self):  # getter
        return self.__saldo

    def setor(self, jumlah):
        if jumlah <= 0:
            print("Jumlah setor harus > 0")
            return
        self.__saldo += jumlah
        print(f"Setor {jumlah} berhasil.")

    def tarik(self, jumlah):
        if jumlah <= 0:
            print("Jumlah tarik harus > 0")
            return
        if jumlah > self.__saldo:
            print("Saldo tidak cukup.")
            return
        self.__saldo -= jumlah
        print(f"Tarik {jumlah} berhasil.")


# 100_000 ==> pemanis visual (digit sparator), mempermudah dalam pembacaan

a = AkunBank("Ujang", 100_000)
print(f"saldo Awal {a.pemilik}: {a.saldo}")
a.__saldo = 100_000_000_000
print("saldo diubah secara paksa: ", a.saldo)
a.setor(-50_000)
print("saldo Setelah stor: ", a.saldo)
a.tarik(300_000_000)
print("Saldo akhir: ", a.saldo)
