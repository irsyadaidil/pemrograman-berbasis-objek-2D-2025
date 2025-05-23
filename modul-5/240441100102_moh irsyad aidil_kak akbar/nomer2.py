from abc import ABC, abstractmethod


class PerangkatElektronik(ABC):
    def __init__(self):
        self.energi_tersisa = 100  

    @abstractmethod
    def nyalakan(self):
        pass

    @abstractmethod
    def matikan(self):
        pass

    @abstractmethod
    def gunakan(self, jam: int):
        pass

    def status(self):
        print(f"Tipe perangkat: {self.__class__.__name__}")
        print(f"Energi tersisa: {self.energi_tersisa}%")
        print("-" * 30)

# Subkelas Laptop
class Laptop(PerangkatElektronik):
    def nyalakan(self):
        print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam: int):
        print(f"Laptop digunakan selama {jam} jam.")
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Baterai laptop habis!")

class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam: int):
        print(f"Kulkas beroperasi selama {jam} jam.")
        self.energi_tersisa -= 5 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
        if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")

def main():
    print("Pilih perangkat yang ingin digunakan:")
    print("1. Laptop")
    print("2. Kulkas")
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == "1":
        perangkat = Laptop()
    elif pilihan == "2":
        perangkat = Kulkas()
    else:
        print("Pilihan tidak valid.")
        return

    while True:
        print("\n=== MENU ===")
        print("1. Nyalakan")
        print("2. Gunakan")
        print("3. Matikan")
        print("4. Tampilkan Status")
        print("5. Keluar")
        aksi = input("Pilih aksi (1-5): ")

        if aksi == "1":
            perangkat.nyalakan()
        elif aksi == "2":
            try:
                jam = int(input("Berapa jam perangkat digunakan? "))
                perangkat.gunakan(jam)
            except ValueError:
                print("Masukkan harus berupa angka.")
        elif aksi == "3":
            perangkat.matikan()
        elif aksi == "4":
            perangkat.status()
        elif aksi == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak dikenal.")


main()
