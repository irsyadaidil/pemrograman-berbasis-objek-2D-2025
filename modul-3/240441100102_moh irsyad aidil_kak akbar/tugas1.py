# tugas praktikum modul 3
class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")


class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan: {self.tunjangan}")
        print("Status: Karyawan Tetap\n")


class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja: {self.jam_kerja} jam/hari")
        print("Status: Karyawan Harian\n")


class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("Daftar Karyawan:")
        for karyawan in self.daftar_karyawan:
            karyawan.info()


manajemen = ManajemenKaryawan()


karyawan1 = KaryawanTetap("Andi", 8000000, "IT", 2000000)
karyawan2 = KaryawanHarian("Budi", 100000, "Produksi", 8)
karyawan3 = KaryawanTetap("Citra", 9000000, "HRD", 2500000)
karyawan4 = KaryawanHarian("Dina", 120000, "Marketing", 7)


manajemen.tambah_karyawan(karyawan1)
manajemen.tambah_karyawan(karyawan2)
manajemen.tambah_karyawan(karyawan3)
manajemen.tambah_karyawan(karyawan4)


manajemen.tampilkan_semua_karyawan()
