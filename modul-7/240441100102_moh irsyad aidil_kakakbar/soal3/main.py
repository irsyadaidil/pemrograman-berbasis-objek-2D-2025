from buku_fiksi import BukuFiksi
from buku_referensi import BukuReferensi

def tampilkan_menu():
    print("\nMenu Sistem Peminjaman Buku")
    print("1. Tambah buku fiksi")
    print("2. Tambah buku referensi")
    print("3. Pinjam buku")
    print("4. Kembalikan buku")
    print("5. Reservasi buku")
    print("6. Keluar")

def cari_buku(daftar_buku, judul):
    for buku in daftar_buku:
        if buku.judul.lower() == judul.lower():
            return buku
    return None

def main():
    daftar_buku = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            judul = input("Masukkan judul buku fiksi: ")
            buku_baru = BukuFiksi(judul)
            daftar_buku.append(buku_baru)
            print(f"Buku fiksi '{judul}' berhasil ditambahkan.")

        elif pilihan == '2':
            judul = input("Masukkan judul buku referensi: ")
            buku_baru = BukuReferensi(judul)
            daftar_buku.append(buku_baru)
            print(f"Buku referensi '{judul}' berhasil ditambahkan.")

        elif pilihan == '3':
            judul = input("Masukkan judul buku yang ingin dipinjam: ")
            buku = cari_buku(daftar_buku, judul)
            if buku:
                nama = input("Masukkan nama peminjam: ")
                buku.pinjam(nama)
            else:
                print("Buku tidak ditemukan.")

        elif pilihan == '4':
            judul = input("Masukkan judul buku yang ingin dikembalikan: ")
            buku = cari_buku(daftar_buku, judul)
            if buku:
                buku.kembalikan()
            else:
                print("Buku tidak ditemukan.")

        elif pilihan == '5':
            judul = input("Masukkan judul buku yang ingin direservasi: ")
            buku = cari_buku(daftar_buku, judul)
            if buku:
                nama = input("Masukkan nama yang ingin reservasi: ")
                buku.reservasi(nama)
            else:
                print("Buku tidak ditemukan.")

        elif pilihan == '6':
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
