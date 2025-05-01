class MataKuliah:
    def __init__(self, kode, nama, sks):
        if MataKuliah.cek_sks(sks) == "valid":
            self.kode = kode
            self.nama = nama
            self.sks = sks
        else:
            print("SKS tidak valid untuk mata kuliah", nama)
            self.kode = kode
            self.nama = nama
            self.sks = 0

    @staticmethod
    def cek_sks(sks):
        if sks == 2 or sks == 3:
            return "valid"
        else:
            return "tidak valid"

    def __str__(self):
        return self.kode + " - " + self.nama + " (" + str(self.sks) + " SKS)"


class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if Mahasiswa.cek_nim(nim) == "valid":
            self.nama = nama
            self.nim = nim
        else:
            print("NIM tidak valid untuk mahasiswa", nama)
            self.nama = nama
            self.nim = "SALAH"
        self.prodi = prodi
        self.matkul_diambil = []
        Mahasiswa.total_mahasiswa = Mahasiswa.total_mahasiswa + 1

    def tambah_matkul(self, matkul):
        self.matkul_diambil.append(matkul)

    def tampilkan_info(self):
        print("\nNama:", self.nama)
        print("NIM:", self.nim)
        print("Prodi:", self.prodi)
        print("Mata Kuliah:")
        for matkul in self.matkul_diambil:
            print(" -", matkul)

    @classmethod
    def jumlah_mahasiswa(cls):
        return cls.total_mahasiswa
    
    @staticmethod
    def cek_nim(nim):
        panjang = len(nim)
        return "valid" if panjang == 10 and nim[0] == '2' and nim[1] == '3' else "tidak valid"





class Kampus:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        cek = Kampus.cek_nama_kampus(nama)
        if cek == "tidak valid":
            print("Nama kampus tidak valid:", nama)

    @classmethod
    def tampilkan_info(cls, nama_kampus):
        print("\nKampus:", nama_kampus)
        print("Total Mahasiswa:", Mahasiswa.jumlah_mahasiswa())

    @staticmethod
    def cek_nama_kampus(nama):
        angka = "0123456789"
        for huruf in nama:
            if huruf in angka:
                return "tidak valid"
        return "valid"


matkul1 = MataKuliah("MK101", "Matematika diskrit", 3)
matkul2 = MataKuliah("MK102", "PBW", 3)
matkul3 = MataKuliah("MK103", "Struktur Data", 3)
matkul4 = MataKuliah("MK104", "Basis Data", 2)
matkul5 = MataKuliah("MK105", "Pemrograman Objek", 3)
matkul6 = MataKuliah("MK106", "Sistem Operasi", 2)
matkul7 = MataKuliah("MK107", " desain manajemen Jaringan", 3)
matkul8 = MataKuliah("MK108", "AI Dasar", 4)  


mhs1 = Mahasiswa("irsyad", "2312345678", "sistem informasi")
mhs2 = Mahasiswa("kiki", "2312345679", "Informatika")
mhs3 = Mahasiswa("arza", "2312345680", "Sistem Informasi")
mhs4 = Mahasiswa("jois", "2312345681", "Informatika")
mhs5 = Mahasiswa("bima", "2312345682", "Teknik Komputer")
mhs6 = Mahasiswa("farhan", "1234567890", "SI")  


for mhs in [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]:
    mhs.tambah_matkul(matkul1)
    mhs.tambah_matkul(matkul2)
    mhs.tambah_matkul(matkul3)
    mhs.tambah_matkul(matkul4)


kampus1 = Kampus("unirvesitas trunojoyo", "Jl. Raya Bangkalan")


print("\n===== DATA MAHASISWA =====")
for mhs in [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]:
    mhs.tampilkan_info()


print("\n===== DATA KAMPUS =====")
Kampus.tampilkan_info(kampus1.nama)
print("Cek nama kampus:", Kampus.cek_nama_kampus(kampus1.nama))
