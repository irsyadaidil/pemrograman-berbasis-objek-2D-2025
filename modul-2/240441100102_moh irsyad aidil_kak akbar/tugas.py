# bagian matkul
class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]


# bagian mhs
class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_diambil = []
        Mahasiswa.total_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.matkul_diambil.append(matkul)

    def tampilkan_info(self):
        print(f"\nMahasiswa: {self.nama} | NIM: {self.nim} | Prodi: {self.prodi}")
        print("Mata Kuliah Diambil:")
        for mk in self.matkul_diambil:
            print(f"- {mk.nama} ({mk.kode}), SKS: {mk.sks}")

    @classmethod
    def get_total_mahasiswa(cls):
        return cls.total_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        panjang = len(nim)
        return panjang == 10 and nim[0] == '2' and nim[1] == '3'



# bagian kampus
class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

    @classmethod
    def tampilkan_info_kampus(cls, nama_kampus):
        print(f"\nKampus: {nama_kampus}")
        print(f"Jumlah Mahasiswa Terdaftar: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nama_kampus(nama):
        for char in nama:
            if char >= '0' and char <= '9':
                return False
        return True


# data kampus
while True:
    nama_kampus = input("masukkan nama kampus: ")
    alamat_kampus = input("masukkan alamat kampus: ")
    if Kampus.validasi_nama_kampus(nama_kampus):
        kampus = Kampus(nama_kampus, alamat_kampus)
        break
    else:
        print("nama kampus tidak valid! Tidak boleh mengandung angka.")

# data matkul
mata_kuliah_list = []
print("\n=== Input Data Mata Kuliah (Minimal 8) ===")
while len(mata_kuliah_list) < 8:
    kode = input("Kode Mata Kuliah: ")
    nama = input("Nama Mata Kuliah: ")
    sks = int(input("Jumlah SKS (2 atau 3): "))
    if MataKuliah.validasi_sks(sks):
        mata_kuliah_list.append(MataKuliah(kode, nama, sks))
    else:
        print("SKS tidak valid. Hanya boleh 2 atau 3.")
    print(f"Total matkul saat ini: {len(mata_kuliah_list)}")

mahasiswa_list = []
print("\n=== Input Data Mahasiswa (Minimal 6) ===")
while len(mahasiswa_list) < 6:
    nama = input("Nama Mahasiswa: ")
    nim = input("NIM (harus 10 digit dan diawali '23'): ")
    prodi = input("Prodi: ")

    if Mahasiswa.validasi_nim(nim):
        mhs = Mahasiswa(nama, nim, prodi)

        print("\nPilih 4 Mata Kuliah (masukkan index):")
        i = 0
        for mk in mata_kuliah_list:
            i += 1
            print(f"{i}. {mk.nama} ({mk.kode}) - SKS: {mk.sks}")

        dipilih = []
        while len(dipilih) < 4:
            idx_input = input(f"Pilih matkul ke-{len(dipilih)+1}: ")
            if idx_input.isdigit():
                index = int(idx_input)
                if 0 <= index < len(mata_kuliah_list) and index not in dipilih:
                    mhs.tambah_matkul(mata_kuliah_list[index])
                    dipilih.append(index)
                else:
                    print("indeks tidak valid atau sudah dipilih.")
            else:
                print("masukkan hanya angka indeks yang valid.")

        mahasiswa_list.append(mhs)
    else:
        print("NIM tidak valid")

    print(f"Total mahasiswa saat ini: {len(mahasiswa_list)}")


print("\n=== Data Mahasiswa dan Mata Kuliah ===")
for mhs in mahasiswa_list:
    mhs.tampilkan_info()

Kampus.jumlah_mahasiswa = Mahasiswa.get_total_mahasiswa()

kampus.tampilkan_info_kampus(kampus.nama)
print(f"apakah nama kampus valid? {"ya" if Kampus.validasi_nama_kampus(kampus.nama) else "tidak"}")

