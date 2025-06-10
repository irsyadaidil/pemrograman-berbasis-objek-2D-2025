from abc import ABC, abstractmethod

class Peminjaman(ABC):
    @abstractmethod
    def pinjam(self, nama_peminjam):
        pass

    @abstractmethod
    def kembalikan(self):
        pass
