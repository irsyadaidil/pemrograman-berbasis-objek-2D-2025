from pembayaran import Pembayaran

class EWallet(Pembayaran):
    def proses_pembayaran(self, jumlah):
        print(f"[EWallet] Membayar sebesar Rp{jumlah:,} via e-wallet (OVO/DANA/Gopay).")
