import math

class BangunDatar:
    def luas(self):
        return 0

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return int(self.sisi * self.sisi)

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * self.jari_jari ** 2

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

def cetak_luas(bangun):
    if isinstance(bangun, Persegi):
        print(f"Luas Persegi adalah: {bangun.luas()}") 
    else:
        print(f"Luas {bangun.__class__.__name__} adalah: {bangun.luas():.2f}") 

def main():
    while True:
        print("\nPilih jenis bangun datar:")
        print("1. Persegi")
        print("2. Lingkaran")
        print("3. Segitiga")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            sisi = int(input("Masukkan panjang sisi: "))
            persegi = Persegi(sisi)
            cetak_luas(persegi)
        elif pilihan == "2":
            jari_jari = int(input("Masukkan jari-jari lingkaran: "))
            lingkaran = Lingkaran(jari_jari)
            cetak_luas(lingkaran)
        elif pilihan == "3":
            alas = int(input("Masukkan alas segitiga: "))
            tinggi = int(input("Masukkan tinggi segitiga: "))
            segitiga = Segitiga(alas, tinggi)
            cetak_luas(segitiga)
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

main()
