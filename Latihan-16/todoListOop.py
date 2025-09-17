class ToDoList:
    def __init__(self):
        self.tugas = [
            "Oded",
            "Udung",
            "Ujang",
            "Ocim",
            "Ocah",
            "Tati",
            "Titi",
            "Tuti",
            "Teti",
        ]

    def tampilkan_menu(self):
        print("=== TO-DO LIST ===")
        print("1. Lihat Tugas")
        print("2. Tambah Tugas")
        print("3. Update Tugas")
        print("4. Cari Tugas")
        print("5. Hapus Tugas")
        print("6. Keluar")

    def lihat_tugas(self):
        if not self.tugas:
            print("Belum ada tugas.")
        else:
            for i, t in enumerate(self.tugas, start=1):
                print(f"{i}. {t}")

    def tambah_tugas(self):
        nama = input("Masukkan nama tugas: ")
        # tugas.append(nama)
        # print("Tugas berhasil ditambahkan!")
        if nama:
            self.tugas.append(nama)
            print("Tugas berhasil ditambahkan!")
        else:
            print("Tugas tidak boleh kosong!")

    def update_tugas(self):
        self.lihat_tugas()
        nomor = int(input("Nomor tugas yang diupdate: "))
        if 1 <= nomor <= len(self.tugas):
            tugasBaru = input("Masukkan tugas baru: ")
            self.tugas[nomor - 1] = tugasBaru
            print("Tugas berhasil diupdate!")
        else:
            print("Nomor tidak valid.")

    def cari_tugas(self):
        keyword = input("Masukkan kata kunci pencarian: ").lower()
        hasil = [t for t in self.tugas if keyword in t.lower()]
        if hasil:
            print("Hasil Pencarian:")
            for h in hasil:
                print("-", h)
            else:
                print("Tidak ada tugas yang cocok.")

    def hapus_tugas(self):
        self.lihat_tugas()
        nomor = int(input("Nomor tugas yang dihapus: "))
        if 1 <= nomor <= len(self.tugas):
            # nomor >= 1 or nomor <= len(tugas)
            self.tugas.pop(nomor - 1)
            print("Tugas berhasil dihapus!")
        else:
            print("Nomor tidak valid.")

    def jalankan(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("Pilih menu (1-6): ")
            if pilihan == "1":
                self.lihat_tugas()
            elif pilihan == "2":
                self.tambah_tugas()
            elif pilihan == "3":
                self.update_tugas()
            elif pilihan == "4":
                self.cari_tugas()
            elif pilihan == "5":
                self.hapus_tugas()
            elif pilihan == "6":
                # print("Program selesai. Sampai jumpa!")
                print(f"Program selesai. Total Tugas: {len(self.tugas)}. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid!")


# Main Program
if __name__ == "__main__":
    app = ToDoList()
    app.jalankan()
