from abc import ABC, abstractmethod

class kendaraan(ABC):
    def __init__(self, nama):
        self.nama

    @abstractmethod
    def kecepatan(self):
        pass
    @abstractmethod
    def roda(self):
        pass
class mobil (kendaraan):
    def roda(self):
        print(F"{self.nama} roda 4")
class sepedahmotor(kendaraan):
    def kecepatan(self):
        print(f"{self.nama} kecepatan 1000")
    def roda (self):
        print(f"{self.nama} roda 2")

ferarri = mobil ("ferarri italia")
harley = sepedahmotor("harley spain")

data_kendaraan = [ferarri,harley]

print(f" kecepatan kendaraan")
for sport in data_kendaraan:
    sport. kecepatan()

print("")
print("")

print(f" kecepatan kendaraan")
for sport in data_kendaraan:
    sport. roda()