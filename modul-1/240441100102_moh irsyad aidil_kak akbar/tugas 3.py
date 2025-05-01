
class Hewan:
    def __init__(self, nama, jenis, suara):
        self.nama = nama
        self.jenis = jenis
        self.suara = suara
    
    def bersuara(self):
        return f"{self.nama} mengeluarkan suara {self.suara}."

class Kucing(Hewan):
    def __init__(self, nama, warna):
        self.nama = nama
        self.jenis = "Kucing"
        self.suara = "Meong"
        self.warna = warna
    
    def info(self):
        return f"{self.nama} adalah kucing berwarna {self.warna}."

    def bersuara(self):
        return f"{self.nama} mengeluarkan suara {self.suara}."

class Anjing(Hewan):
    def __init__(self, nama, ras):
        self.nama = nama
        self.jenis = "Anjing"
        self.suara = "Guk-guk"
        self.ras = ras

    def info(self):
        return f"{self.nama} adalah anjing ras {self.ras}."

    def bersuara(self):
        return f"{self.nama} mengeluarkan suara {self.suara}."

class Burung(Hewan):
    def __init__(self, nama, bisa_terbang):
        self.nama = nama
        self.jenis = "Burung"
        self.suara = "Cuit-cuit"
        self.bisa_terbang = bisa_terbang

    def info(self):
        kemampuan = "bisa terbang" if self.bisa_terbang else "tidak bisa terbang"
        return f"{self.nama} adalah burung yang {kemampuan}."

    def bersuara(self):
        return f"{self.nama} mengeluarkan suara {self.suara}."


# Membuat objek menggunakan looping
hewan_list = []
data_hewan = [
    ("jony", "Putih", "Kucing"),
    ("jeny", "Labrador", "Anjing"),
    ("jono", True, "Burung")
]

for data in data_hewan:
    if data[2] == "Kucing":
        hewan_list.append(Kucing(data[0], data[1]))
    elif data[2] == "Anjing":
        hewan_list.append(Anjing(data[0], data[1]))
    elif data[2] == "Burung":
        hewan_list.append(Burung(data[0], data[1]))

# Menampilkan informasi hewan
for hewan in hewan_list:
    print(hewan.info())
    print(hewan.bersuara())
    print()