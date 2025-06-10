from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def main():
    print("=== Sistem Pemesanan Kendaraan ===")
    nama = input("Masukkan nama Anda: ")
    
    try:
        usia = int(input("Masukkan usia Anda: "))
    except ValueError:
        print("Usia harus berupa angka.")
        return

    print("\nPilih jenis kendaraan:")
    print("1. Mobil")
    print("2. Motor")
    print("3. Sepeda")
    pilihan = input("Pilihan (1/2/3): ")

    if pilihan == "1":
        kendaraan = Mobil()
    elif pilihan == "2":
        kendaraan = Motor()
    elif pilihan == "3":
        kendaraan = Sepeda()
    else:
        print("Pilihan tidak valid.")
        return

    print(f"\n👤 Pemesan: {nama} (Usia: {usia})")
    if kendaraan.pesan(usia):
        kendaraan.hitung_biaya()
        kendaraan.info_asuransi()

if __name__ == "__main__":
    main()
