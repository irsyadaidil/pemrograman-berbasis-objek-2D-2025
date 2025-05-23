class Manusia:
    def berbicara(self):
        print("Manusia berbicara...")

    def bekerja(self):
        print("Manusia bekerja...")

    def makan(self):
        print("Manusia makan...")

class irsyad(Manusia):
    def berbicara(self):
        print("irsyad berbicara dengan suara lantang dan percaya diri.")

    def bekerja(self):
        print("irsyad bekerja sebagai insinyur di proyek besar.")

    def makan(self):
        print("irsyad makan dengan cepat karena sibuk.")

class kiki(Manusia):
    def berbicara(self):
        print("kiki berbicara dengan tenang dan hati-hati.")

    def bekerja(self):
        print("kiki bekerja sebagai guru di sekolah dasar.")

    def makan(self):
        print("kiki makan dengan perlahan sambil membaca buku.")

class bima(Manusia):
    def berbicara(self):
        print("bima berbicara dengan ceria dan penuh semangat.")

    def bekerja(self):
        print("bima bekerja sebagai desainer grafis kreatif.")

    def makan(self):
        print("bima makan sambil mencoba makanan baru dari berbagai negara.")

class arza(Manusia):
    def berbicara(self):
        print("arza berbicara dengan suara lembut dan sopan.")

    def bekerja(self):
        print("arza bekerja dari rumah sebagai penulis konten.")

    def makan(self):
        print("arza makan makanan sehat dan organik setiap hari.")

karakter_dict = {
    "irsyad": irsyad,
    "kiki": kiki,
    "bima": bima,
    "arza": arza
}

def main():
    print("Karakter yang tersedia: irsyad, kiki, bima, arza")
    print("Ketik 'keluar' untuk menghentikan program.")
    while True:
        nama = input("Masukkan nama karakter yang ingin dilihat (tanpa huruf kapital): ").lower()

        if nama == "keluar":
            print("Program dihentikan.")
            break

        karakter = karakter_dict.get(nama)
        if karakter:
            objek = karakter()
            objek.berbicara()
            objek.bekerja()
            objek.makan()
            print("Program dihentikan setelah menampilkan karakter.")
            break
        else:
            print("Karakter tidak ditemukan. Coba lagi.")


main()
