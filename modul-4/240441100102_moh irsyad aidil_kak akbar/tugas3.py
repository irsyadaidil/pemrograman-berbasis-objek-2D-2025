class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    def get_data(self):
        return f"Nama: {self.__nama}, Umur: {self.__umur}, Keluhan: {self.__keluhan}"


class Klinik:
    def __init__(self):
        self.__daftar_pasien = []

    def tambah_pasien(self, pasien):
        self.__daftar_pasien.append(pasien)
        print("✅ Pasien berhasil ditambahkan!\n")

    def tampilkan_pasien(self):
        print("📋 Daftar Pasien:")
        if not self.__daftar_pasien:
            print("Belum ada pasien yang terdaftar.\n")
        else:
            for i, pasien in enumerate(self.__daftar_pasien, start=1):
                print(f"{i}. {pasien.get_data()}")
            print()


def main():
    klinik = Klinik()

    while True:
        print("=== MENU KLINIK ===")
        print("1. Tambah Pasien")
        print("2. Tampilkan Daftar Pasien")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            nama = input("Masukkan nama pasien: ")
            umur = input("Masukkan umur pasien: ")
            keluhan = input("Masukkan keluhan pasien: ")
            pasien_baru = Pasien(nama, umur, keluhan)
            klinik.tambah_pasien(pasien_baru)

        elif pilihan == '2':
            klinik.tampilkan_pasien()

        elif pilihan == '3':
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")


main()
