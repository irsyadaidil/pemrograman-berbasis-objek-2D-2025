from kendaraan import PesanKendaraan

class Sepeda(PesanKendaraan):
    def __init__(self):
        self.biaya = 50000

    def pesan(self, usia_pengguna):
        if usia_pengguna < 12:
            print(" Usia minimal untuk sewa sepeda adalah 12 tahun.")
            return False
        print("Sepeda berhasil dipesan.")
        return True

    def hitung_biaya(self):
        print(f" Biaya sewa sepeda: Rp{self.biaya:,}")

    def info_asuransi(self):
        print(" Tidak termasuk asuransi untuk sepeda.")
