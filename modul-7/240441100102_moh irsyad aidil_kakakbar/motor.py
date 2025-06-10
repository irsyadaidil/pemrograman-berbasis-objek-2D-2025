from pembayaran import Pembayaran

class TransferBank(Pembayaran):
    def proses_pembayaran(self, jumlah):
        print(f"[TransferBank] Membayar sebesar Rp{jumlah:,} via transfer bank.")
