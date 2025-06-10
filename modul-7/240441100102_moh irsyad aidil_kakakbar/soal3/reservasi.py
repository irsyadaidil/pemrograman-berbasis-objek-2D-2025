from abc import ABC, abstractmethod

class Reservasi(ABC):
    @abstractmethod
    def reservasi(self, nama_reservasi):
        pass
