from kendaraan import PesanKendaraan

class Mobil(PesanKendaraan):
    def __init__(self):
        self.biaya = 500000

    def pesan(self, usia_pengguna):
        if usia_pengguna < 21:
            print(" Usia minimal untuk sewa mobil adalah 21 tahun.")
            return False
        print(" Mobil berhasil dipesan.")
        return True

    def hitung_biaya(self):
        print(f" Biaya sewa mobil: Rp{self.biaya:,}")

    def info_asuransi(self):
        print(" Asuransi all-risk mobil termasuk dalam harga.")
