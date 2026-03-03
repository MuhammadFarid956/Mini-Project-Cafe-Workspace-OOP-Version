from entity import Entity
from master_data import MasterData
import csv
import os

class Paket(Entity, MasterData):
    def __init__(self, package, type_pack, minimum_order, price):
        MasterData.__init__(self, "paket_data.csv", ["ID", "Package Name", "Type", "min_order/org", "Price Paket"])
        self.filename = "paket_data.csv"
        self.prefix = "P"
        self.package_name = package
        self.type = type_pack
        self.min = minimum_order
        self.price = price
        self.id = Entity.gen_id(self.filename, self.prefix)

    def add_package(self):
        print("==== Add Package ====")
        id_pack = self.id
        self.package_name = input("Package Name: ")
        self.type = input("Package Type: ")
        self.min = input("Minimum Order: ")
        self.price = input("Price: ")

        with open(self.filename, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id_pack, self.package_name, self.type, self.min, self.price])
        print("Successfully Added Package")

    def show_pack(self):
        print("===== Show Pack ====")
        super().show()


if __name__ == "__main__":
    paket = Paket("Paket", "Paket", 1, 100)
    paket.add_package()
    print(paket.__dict__)
