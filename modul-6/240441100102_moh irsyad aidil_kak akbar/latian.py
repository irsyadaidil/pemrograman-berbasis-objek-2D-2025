# class Binatang:
#     def bersuara(self):
#         pass

# class Anjing(Binatang):
#     def bersuara(self):
#         return "Woof!"

# class Kucing(Binatang):
#     def bersuara(self):
#      return "Meow!"

# def suara_hewan(hewan):
#     return hewan.bersuara()

# anjing = Anjing()
# kucing = Kucing()

# print(suara_hewan(anjing)) # Output: Woof!
# print(suara_hewan(kucing)) # Output: Meow!


# class Bebek:
#     def suara(self):
#         return "Kwek kwek"
# class Angsa:
#     def suara(self):
#         return "Kriik kriik"
# def buat_suara(hewan):
#     print(hewan.suara())
# bebek = Bebek()
# angsa = Angsa()
# buat_suara(bebek) # Output: Kwek kwek
# buat_suara(angsa) # Output: Kriik kriik


# class Titik:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# def __add__(self, other):
#     return Titik(self.x + other.x, self.y + other.y)
# def __str__(self):
#     return f"({self.x}, {self.y})"

# t1 = Titik(1, 2)
# t2 = Titik(3, 4)
# t3 = t1 + t2

# print(t3)

# class Kalkulator:
#     def tambah(self, a, b, c=0):
#         return a + b + c
    
# calc = Kalkulator()
# print(calc.tambah(2, 3)) # Output: 5
# print(calc.tambah(2, 3, 4))

class Binatang:
    def suara(self):
        return "Suara binatang"
class Anjing(Binatang):
    def suara(self):
        return "Guk guk"
class Kucing(Binatang):
    def suara(self):
        return "Meong"
def buat_suara(hewan):
    print(hewan.suara())
    
anjing = Anjing()
kucing = Kucing()
buat_suara(anjing) # Output: Guk guk
buat_suara(kucing)