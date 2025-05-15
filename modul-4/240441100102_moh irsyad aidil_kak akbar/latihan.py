class mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.__nama= nama
        self.__nim = nim
        self.__prodi = prodi

    def setNama(self,namabaru):
        self.__nama = namabaru

    def setnim(self,nimbaru):
        self.__nim = nimbaru
    
    def setprodi(self, prodibaru):
        self.__prodi = prodibaru
    def getnama(self):
        return self.__nama
    def getnama(self):
        return self.__nim
    def getnama(self):
        return self.__prodi
    def infodetailmhs(self):
        print(f"nama saya : {self.getnama()}")

mhs1 = mahasiswa("putri", 24568821,"sistem informasi")
mhs1.setNama("tiara")
print(f"nama :{mhs1}.get.nama()")

# print(mhs1.nama)
# print(mhs1._nim)
# print(mhs1.__prodi)

