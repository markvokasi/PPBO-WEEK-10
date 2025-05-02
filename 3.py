from abc import ABC, abstractmethod

class Ban(ABC):
    @abstractmethod
    def karakteristik(self):
        pass

class SoftBan(Ban):
    def karakteristik(self):
        print("Soft Tire: Paling cepat, namun cepat Habis/tipis.")

class MediumBan(Ban):
    def karakteristik(self):
        print("Medium Tire: Seimbang antara kecepatan dan daya tahan.")

class HardBan(Ban):
    def karakteristik(self):
        print("Hard Tire: Paling awet, namun cengkramannya kurang.")

# Factory class
class BanFactory(ABC):
    def __init__(self):
        self.ban = []
        self.createBan()

    @abstractmethod
    def createBan(self):
        pass

    def getBan(self):
        return self.ban

    def addBan(self, ban):
        self.ban.append(ban)

class Soft(BanFactory):
    def createBan(self):
        self.addBan(SoftBan())

class Medium(BanFactory):
    def createBan(self):
        self.addBan(MediumBan())

class Hard(BanFactory):
    def createBan(self):
        self.addBan(HardBan())

ban_type = input("Pilih jenis ban F1 (Soft, Medium, Hard): ")
ban_selected = eval(ban_type.capitalize())()
print(f"\nJenis Ban {type(ban_selected).__name__} dipilih.")
print("Karakteristik Ban:")
for ban in ban_selected.getBan():
    ban.karakteristik()

