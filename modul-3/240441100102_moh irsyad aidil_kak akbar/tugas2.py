# tugas praktikum modul 3
class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5  



class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        if self.jenis_kendaraan == "motor":
            return 6  # 
        elif self.jenis_kendaraan == "mobil":
            return 4  
        else:
            return super().estimasi_waktu() 



class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "citilink":
            return 2  
        elif self.maskapai == "air asia":
            return 3  
        else:
            return super().estimasi_waktu() 



class PengirimanInternasional(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        super().__init__(asal, tujuan)
        self.pengiriman_darat = PengirimanDarat(asal, tujuan, jenis_kendaraan)
        self.pengiriman_udara = PengirimanUdara(asal, tujuan, maskapai)

    def estimasi_waktu(self):
        waktu_darat = self.pengiriman_darat.estimasi_waktu()
        waktu_udara = self.pengiriman_udara.estimasi_waktu()
        
        
        if waktu_darat < waktu_udara:
            waktu_tercepat = waktu_darat
        else:
            waktu_tercepat = waktu_udara

        if self.tujuan.lower() != "indonesia":
            waktu_tercepat += 3

        return waktu_tercepat


pengiriman1 = PengirimanInternasional("Jakarta", "Singapura", "mobil", "citilink")
pengiriman2 = PengirimanInternasional("Surabaya", "Indonesia", "motor", "air asia")
pengiriman3 = PengirimanInternasional("Medan", "Malaysia", "mobil", "air asia")

print("Estimasi Pengiriman 1:", pengiriman1.estimasi_waktu(),  "hari")
print("Estimasi Pengiriman 1:", pengiriman1.asal,  "hari")
print("Estimasi Pengiriman 2:", pengiriman2.estimasi_waktu(), "hari")
print("Estimasi Pengiriman 3:", pengiriman3.estimasi_waktu(), "hari")
