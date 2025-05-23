
# class Karyawan:
#     def __init__(self, nama, gaji, departemen):
#         self.nama = nama
#         self.gaji = gaji
#         self.departemen = departemen

#     def info(self):
#         print(f"Nama: {self.nama}")
#         print(f"Gaji: {self.gaji}")
#         print(f"Departemen: {self.departemen}")


# class KaryawanTetap(Karyawan):
#     def __init__(self, nama, gaji, departemen, tunjangan):
#         super().__init__(nama, gaji, departemen)
#         self.tunjangan = tunjangan

#     def info(self):
#         super().info()
#         print(f"Tunjangan: {self.tunjangan}")
#         print("Status: Karyawan Tetap\n")


# class KaryawanHarian(Karyawan):
#     def __init__(self, nama, gaji, departemen, jam_kerja):
#         super().__init__(nama, gaji, departemen)
#         self.jam_kerja = jam_kerja

#     def info(self):
#         super().info()
#         print(f"Jam Kerja: {self.jam_kerja} jam/hari")
#         print("Status: Karyawan Harian\n")


# class ManajemenKaryawan:
#     def __init__(self):
#         self.daftar_karyawan = []

#     def tambah_karyawan(self, karyawan):
#         self.daftar_karyawan.append(karyawan)

#     def tampilkan_semua_karyawan(self):
#         print("Daftar Karyawan:")
#         for karyawan in self.daftar_karyawan:
#             karyawan.info()


# manajemen = ManajemenKaryawan()


# karyawan1 = KaryawanTetap("kiki", 8000000, "IT", 2000000)
# karyawan2 = KaryawanHarian("irsyad", 100000, "Produksi", 8)
# karyawan3 = KaryawanTetap("bima", 9000000, "HRD", 2500000)
# karyawan4 = KaryawanHarian("arz", 120000, "Marketing", 7)


# manajemen.tambah_karyawan(karyawan1)
# manajemen.tambah_karyawan(karyawan2)
# manajemen.tambah_karyawan(karyawan3)
# manajemen.tambah_karyawan(karyawan4)


# manajemen.tampilkan_semua_karyawan()


# # latihan 2
# # tugas praktikum modul 3
# class Pengiriman:
#     def __init__(self, asal, tujuan):
#         self.asal = asal
#         self.tujuan = tujuan

#     def estimasi_waktu(self):
#         return 5  



# class PengirimanDarat(Pengiriman):
#     def __init__(self, asal, tujuan, jenis_kendaraan):
#         super().__init__(asal, tujuan)
#         self.jenis_kendaraan = jenis_kendaraan

#     def estimasi_waktu(self):
#         if self.jenis_kendaraan == "motor":
#             return 6  # 
#         elif self.jenis_kendaraan == "mobil":
#             return 4  
#         else:
#             return super().estimasi_waktu() 



# class PengirimanUdara(Pengiriman):
#     def __init__(self, asal, tujuan, maskapai):
#         super().__init__(asal, tujuan)
#         self.maskapai = maskapai

#     def estimasi_waktu(self):
#         if self.maskapai == "citilink":
#             return 2  
#         elif self.maskapai == "air asia":
#             return 3  
#         else:
#             return super().estimasi_waktu() 



# class PengirimanInternasional(Pengiriman):
#     def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
#         super().__init__(asal, tujuan)
#         self.pengiriman_darat = PengirimanDarat(asal, tujuan, jenis_kendaraan)
#         self.pengiriman_udara = PengirimanUdara(asal, tujuan, maskapai)

#     def estimasi_waktu(self):
#         waktu_darat = self.pengiriman_darat.estimasi_waktu()
#         waktu_udara = self.pengiriman_udara.estimasi_waktu()
        
        
#         if waktu_darat < waktu_udara:
#             waktu_tercepat = waktu_darat
#         else:
#             waktu_tercepat = waktu_udara

#         if self.tujuan.lower() != "indonesia":
#             waktu_tercepat += 3

#         return waktu_tercepat


# pengiriman1 = PengirimanInternasional("Jakarta", "Singapura", "mobil", "citilink")
# pengiriman2 = PengirimanInternasional("Surabaya", "Indonesia", "motor", "air asia")
# pengiriman3 = PengirimanInternasional("Medan", "Malaysia", "mobil", "air asia")

# print("Estimasi Pengiriman 1:", pengiriman1.estimasi_waktu(),  "hari")
# print("Estimasi Pengiriman 1:", pengiriman1.asal,  "hari")
# print("Estimasi Pengiriman 2:", pengiriman2.estimasi_waktu(), "hari")
# print("Estimasi Pengiriman 3:", pengiriman3.estimasi_waktu(), "hari")

# class mobil:
#     def __init__ (self, merk,warna,tahun):
#         self.merk = merk
#         self.warna = warna
#         self.tahun = tahun
#     def info(self):
#         print(f"mobil : {self.merk}")
#         print(f"warna : {self.warna}")
#         print(f"tahun : {self.tahun}")

# mobil1 = mobil("Toyota","merah", 2020)
# mobil1.info()
# class hewan :
#     def __init__(self, nama):
#         self.nama = nama
#     def bersuara(self):
#         print(f"hewan bersuara")
# class kucing(hewan):
#     def bersuara(self):
#         print("meong")

# kucing1 = kucing("kitty")
# kucing1.bersuara()
        