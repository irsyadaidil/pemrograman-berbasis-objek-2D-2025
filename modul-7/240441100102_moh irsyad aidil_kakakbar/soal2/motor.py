from kendaraan import PesanKendaraan

class Motor(PesanKendaraan):
    def __init__(self):
        self.biaya = 150000

    def pesan(self, usia_pengguna):
        if usia_pengguna < 17:
            print("Usia minimal untuk sewa motor adalah 17 tahun.")
            return False
        print(" Motor berhasil dipesan.")
        return True

    def hitung_biaya(self):
        print(f" Biaya sewa motor: Rp{self.biaya:,}")

    def info_asuransi(self):
        print(" Asuransi dasar motor disediakan.")
