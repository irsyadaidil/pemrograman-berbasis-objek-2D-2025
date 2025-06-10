from abc import ABC, abstractmethod

class PesanKendaraan(ABC):
    @abstractmethod
    def pesan(self, usia_pengguna):
        pass

    @abstractmethod
    def hitung_biaya(self):
        pass

    @abstractmethod
    def info_asuransi(self):
        pass
