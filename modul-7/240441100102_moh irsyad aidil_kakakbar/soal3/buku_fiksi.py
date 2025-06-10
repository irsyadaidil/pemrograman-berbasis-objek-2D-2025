from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuFiksi(Peminjaman, Reservasi):
    def __init__(self, judul):
        self.judul = judul
        self.status_pinjam = False
        self.status_reservasi = False
        self.reservasi_oleh = None

    def pinjam(self, nama_peminjam):
        if self.status_pinjam:
            print(f"Buku '{self.judul}' sedang dipinjam, tidak bisa dipinjam lagi.")
            return False
        if self.status_reservasi and self.reservasi_oleh != nama_peminjam:
            print(f"Buku '{self.judul}' sudah direservasi oleh orang lain.")
            return False
        self.status_pinjam = True
        self.status_reservasi = False
        self.reservasi_oleh = None
        print(f"{nama_peminjam} berhasil meminjam buku fiksi '{self.judul}'.")
        return True

    def kembalikan(self):
        if not self.status_pinjam:
            print(f"Buku '{self.judul}' belum dipinjam.")
            return False
        self.status_pinjam = False
        print(f"Buku fiksi '{self.judul}' sudah dikembalikan.")
        return True

    def reservasi(self, nama_reservasi):
        if self.status_reservasi:
            print(f"Buku '{self.judul}' sudah direservasi.")
            return False
        if self.status_pinjam:
            self.status_reservasi = True
            self.reservasi_oleh = nama_reservasi
            print(f"{nama_reservasi} berhasil mereservasi buku fiksi '{self.judul}'.")
            return True
        else:
            print(f"Buku '{self.judul}' tersedia, tidak perlu reservasi.")
            return False
