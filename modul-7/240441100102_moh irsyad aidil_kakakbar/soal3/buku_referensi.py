from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuReferensi(Peminjaman, Reservasi):
    def __init__(self, judul):
        self.judul = judul

    def pinjam(self, nama_peminjam):
        print(f"Buku referensi '{self.judul}' tidak bisa dipinjam.")
        return False

    def kembalikan(self):
        print(f"Buku referensi '{self.judul}' tidak dipinjam, jadi tidak bisa dikembalikan.")
        return False

    def reservasi(self, nama_reservasi):
        print(f"Buku referensi '{self.judul}' tidak bisa direservasi.")
        return False
