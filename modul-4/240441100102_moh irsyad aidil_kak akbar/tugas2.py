
class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_jumlah_halaman(self):
        return self.__jumlah_halaman


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print("✅ Buku berhasil ditambahkan ke perpustakaan.")

    def tampilkan_buku(self):
        if self.daftar_buku:
            print("\n📚 Daftar Buku di Perpustakaan:")
            for i, buku in enumerate(self.daftar_buku, start=1):
                print(f"{i}. Judul: {buku.get_judul()}, Penulis: {buku.get_penulis()}, Halaman: {buku.get_jumlah_halaman()}")
        else:
            print("❌ Tidak ada buku di perpustakaan.")

def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\n=== MENU PERPUSTAKAAN ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Daftar Buku")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            judul = input("Masukkan Judul Buku: ")
            penulis = input("Masukkan Nama Penulis: ")
            try:
                halaman = int(input("Masukkan Jumlah Halaman: "))
                buku_baru = Buku(judul, penulis, halaman)
                perpustakaan.tambah_buku(buku_baru)
            except ValueError:
                print("❌ Jumlah halaman harus berupa angka!")

        elif pilihan == '2':
            perpustakaan.tampilkan_buku()

        elif pilihan == '3':
            print("👋 Terima kasih telah menggunakan sistem perpustakaan.")
            break

        else:
            print("❌ Pilihan tidak valid. Coba lagi.")

main()
