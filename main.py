import random
import csv
class Bullet:
    def __init__(self,number, calibr, weight):
        self.number = number
        self.calibr = calibr
        self.weight = weight
        self.power = self.calibr * self.weight
    def __repr__(self):
        return f"Снаряд {self.number} имеет следующие характеристики:" \
               f" Калибр:{self.calibr}, Масса:{self.weight}, Мощность:{self.power}" \
               f""
class Clip_stack:
    def __init__(self):
        self.stack = []
    def append(self, bullet):
        self.stack.insert(0, bullet)
    def remove(self):
        self.stack.pop(0)
    def show(self):
        return self.stack

    def get_info(self):
        with open("info.csv", "a", newline='') as file:
            writer = csv.writer(file, delimiter=';', lineterminator="")
            writer.writerow(self.show())
    def create_file(self):
        with open("info.csv", "w", ) as file:
            pass
Magaz= Clip_stack()
Magaz.create_file()
n = int(input())
for i in range(1, n + 1):
    bullet_i = Bullet(i, random.randint(6, 20), random.randint(1, 100))
    Magaz.append(bullet_i)
print(Magaz.show())
Magaz.remove()
print(Magaz.show())
Magaz.get_info()