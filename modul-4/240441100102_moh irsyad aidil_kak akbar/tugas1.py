
class RekeningBank:
    def __init__(self, no_rek, nama_pemilik, saldo):
        self.__no_rek = no_rek
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    def get_no_rek(self):
        return self.__no_rek

    def get_nama_pemilik(self):
        return self.__nama_pemilik

    def get_saldo(self):
        return self.__saldo

    def setor_tunai(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"✅ Setor tunai sebesar {jumlah} berhasil. Saldo sekarang: {self.__saldo}")
        else:
            print("❌ Jumlah setor tunai tidak valid.")

    def tarik_tunai(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"✅ Tarik tunai sebesar {jumlah} berhasil. Saldo sekarang: {self.__saldo}")
        else:
            print("❌ Jumlah tarik tunai tidak valid atau saldo tidak cukup.")

class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self, rekening):
        self.rekening_list.append(rekening)
        print("✅ Rekening berhasil ditambahkan.")

    def cari_rekening(self, no_rek):
        for rekening in self.rekening_list:
            if rekening.get_no_rek() == no_rek:
                return rekening
        return None

    def tampilkan_rekening(self):
        if self.rekening_list:
            print("\n📋 Daftar Rekening Bank:")
            for rekening in self.rekening_list:
                print(f"- No Rek: {rekening.get_no_rek()}, Nama: {rekening.get_nama_pemilik()}, Saldo: {rekening.get_saldo()}")
        else:
            print("❌ Belum ada rekening yang tersedia.")


def main():
    bank = Bank()

    while True:
        print("\n=== MENU BANK ===")
        print("1. Tambah Rekening")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Tampilkan Semua Rekening")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            no_rek = input("Masukkan No Rekening: ")
            nama = input("Masukkan Nama Pemilik: ")
            saldo_awal = float(input("Masukkan Saldo Awal: "))
            rekening_baru = RekeningBank(no_rek, nama, saldo_awal)
            bank.tambah_rekening(rekening_baru)

        elif pilihan == '2':
            no_rek = input("Masukkan No Rekening: ")
            rekening = bank.cari_rekening(no_rek)
            if rekening:
                jumlah = float(input("Masukkan jumlah setor: "))
                rekening.setor_tunai(jumlah)
            else:
                print("❌ Rekening tidak ditemukan.")

        elif pilihan == '3':
            no_rek = input("Masukkan No Rekening: ")
            rekening = bank.cari_rekening(no_rek)
            if rekening:
                jumlah = float(input("Masukkan jumlah tarik: "))
                rekening.tarik_tunai(jumlah)
            else:
                print("❌ Rekening tidak ditemukan.")

        elif pilihan == '4':
            bank.tampilkan_rekening()

        elif pilihan == '5':
            print("👋 Terima kasih telah menggunakan layanan bank.")
            break

        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
main()
