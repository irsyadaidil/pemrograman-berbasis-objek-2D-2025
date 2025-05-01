# # intance method

# # class siswa:
# #     def __init__(self, nama):
# #         self.nama = nama
    
# #     def sapa(self):
# #         print(f"halo, saya {self.nama}")

# #     def belajar(self):
# #         print(f"{self.nama} sedang belajar")

# #     def ubah_nama(self, baru):
# #         self.nama = baru

# #     def tampilkan_nama(self):
# #         print("nama siswa:",self.nama)

# #     def perkenalan(self):
# #         print(f"perkenalan,saya {self.nama} dari kelas 10")

# # #buat objek
# # siswa1 = siswa("jono")

# # #cara manggilnya
# # siswa1.sapa()
# # siswa1.belajar()
# # siswa1.ubah_nama("jamal")
# # siswa1.tampilkan_nama()
# # siswa1.perkenalan()
        
# # #CLAS METHOD
# # class sekolah :
# #     nama_sekolah = "sma negeri 1"

# #     @classmethod
# #     def tampilkan_nama(cls):
# #         print(cls.nama_sekolah)
    
# #     @classmethod
# #     def ubah_nama(cls,baru):
# #         cls.nama_sekolah = baru

# #     @classmethod
# #     def info(cls):
# #         print(f" selamat datang di {cls.nama_sekolah}")

# #     @classmethod
# #     def panjang_nama(cls):
# #         return len(cls.nama_sekolah)

# #     @classmethod
# #     def huruf_besar(cls):
# #        return cls.nama_sekolah.upper()
# # #cara memanggilnya
# # sekolah.tampilkan_nama()
# # sekolah.ubah_nama("sma jaya")
# # sekolah.info()
# # print(sekolah.panjang_nama())
# # print(sekolah.huruf_besar())


# #staticmethod
# class matematika :
#     @staticmethod
#     def tambah(a,b):
#         return a + b 
    
#     @staticmethod
#     def kali(a,b):
#         return a*b
#     @staticmethod
#     def pangkat(angka,b):
#         return angka**b
#     @staticmethod
#     def luas_persegi(sisi):
#         return sisi*sisi
#     @staticmethod
#     def cek_genap(angka):
#         return angka %2==0
    
# #cara manggilnya
# print (matematika.tambah(2,6))
# print (matematika.kali(8,9))
# print (matematika.pangkat(3,4))
# print (matematika.luas_persegi(40))
# print (matematika. cek_genap(4))






        
#     # Parent class: Hewan
# class Hewan:
#     def __init__(self, nama, health):
#         self.nama = nama
#         self.health = 100

#     def makan(self):
#         print(f"{self.nama} sedang makan")
#     def jalan (self):
#         print(f"{self.nama}sedang jalan")

# class Dog (Hewan):
#     pass

# dog = Dog("Blaky")
# print(dog.mame)
# print(dog.health)
# dog.makan()
# dog.jalan()

class Hewan:
    def bersuara (self):
        print("hewan bersuara")
class kucing (Hewan):
    def bersuara(self):
        print("meong")
class Anjing ( Hewan):
    def bersuara(self):
        print("guk guk")

suara = Hewan()
kucing = kucing()
Anjing = Anjing()

suara.bersuara()
kucing.bersuara()
Anjing.bersuara()


class Hewan:
    def __init__(self, nama):
        self.nama = nama
        print(f"Hewan bernama {self.nama} dibuat.")

class Kucing(Hewan):
    def __init__(self, nama, warna):
        super().__init__(nama)
        self.warna = warna
        print(f"Kucing warna {self.warna} dibuat.")

Kucing("Kitty", "Putih")


class Hewan:
    def makan(self):
        print("Hewan sedang makan.")

class Kelinci(Hewan):
    def makan(self):
        super().makan()
        print("Tapi dia makan wortel 🥕")

Kelinci().makan()
