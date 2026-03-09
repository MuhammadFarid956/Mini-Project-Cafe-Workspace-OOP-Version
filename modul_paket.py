# from entity import Entity
# from master_data import MasterData
# import csv
#
# class Paket(Entity, MasterData):
#     def __init__(self, package, type_pack, minimum_order, price):
#         MasterData.__init__(self, "paket_data.csv", ["ID", "Package Name", "Type", "min_order/org", "Price Paket"])
#         self.filename = "paket_data.csv"
#         self.prefix = "P"
#         self.package_name = package
#         self.type = type_pack
#         self.min = minimum_order
#         self.price = price
#         self.id = Entity.gen_id(self.filename, self.prefix)
#
#     def add_package(self):
#         print("==== Add Package ====")
#         id_pack = self.id
#         self.package_name = input("Package Name: ")
#         self.type = input("Package Type: ")
#         self.min = input("Minimum Order: ")
#         self.price = input("Price: ")
#
#         with open(self.filename, "a", newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow([id_pack, self.package_name, self.type, self.min, self.price])
#         print("Successfully Added Package")
#
#     def show_pack(self):
#         print("===== Show Pack ====")
#         super().show()
#
#
# if __name__ == "__main__":
#     paket = Paket("Paket", "Paket", 1, 100)
#     paket.add_package()
#     print(paket.__dict__)

import csv
import os

class PackageManager:
    def __init__(self, filename='paket_data.csv'):
        self.filename = filename

    def next_id(self):
        last_num = 0
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as p:
                reader = csv.reader(p)
                for row in reader:
                    if row and row[0].startswith('P'):
                        num = int(row[0].replace('P', ''))
                        if num > last_num:
                            last_num = num
        return f'P{last_num + 1:03d}'

    def show(self):
        print('================= Package =================')
        if not os.path.exists(self.filename):
            print('File Not Found')
            return

        with open(self.filename, 'r') as p:
            reader = csv.reader(p)
            print(f'{"ID":<5} | {"Name":<20} | {"Type":<10} | {"Min Order/Person":<20} | {"Capacity":<10} | {"Duration":<10} | {"Price":>12}')
            print('='*106)
            for row in reader:
                if row:
                    print(f'{row[0]:<5} | {row[1]:<20} | {row[2]:<10} | {row[3]:<20} | {row[4]:<10} | {row[5]:<10} | {row[6]:>12}')

    def add(self):
        print('================= Add Package =================')
        id_package = self.next_id()
        name = input('Enter Package Name: ')
        type_pack = input('Enter Package Type: ')
        min_order = int(input('Enter Package Min Order/Person: '))
        capacity = int(input('Enter Package Capacity: '))
        duration = int(input('Enter Package Duration: '))
        price = int(input('Enter Package Price: '))

        with open(self.filename, 'a', newline='') as p:
            writer = csv.writer(p)
            writer.writerow([id_package, name, type_pack, min_order, capacity, duration, price])
        print('Package Added')

    def update(self):
        print('================== Update Package =================')
        self.show()
        target =input('Enter Package ID: ').upper()
        temporary_data = []
        found = False
        with open(self.filename, 'r') as p:
            reader = csv.reader(p)
            for row in reader:
                if row and row[0] == target:
                    print(f'================= Package Information =================')
                    print(f'Name : {row[1]}\nType : {row[2]}\nMin Order/Person : {row[3]}\nCapacity : {row[4]}\nDuration : {row[5]}\nPrice : {row[6]}')

                    new_min_order = input('Enter Package Min Order/Person (Click Enter to Continue): ')
                    new_capacity = input('Enter Package Capacity (Click Enter to Continue): ')
                    new_duration = input('Enter Package Duration (Click Enter to Continue): ')
                    new_price = input('Enter Package Price (Click Enter to Continue): ')

                    if len(new_min_order )> 0:
                        row[3] = int(new_min_order)
                    if len(new_capacity) > 0:
                        row[4] = int(new_capacity)
                    if len(new_duration) > 0:
                        row[5] = int(new_duration)
                    if len(new_price)> 0:
                        row[6] = int(new_price)
                    found = True
                temporary_data.append(row)

        if found:
            with open(self.filename, 'w', newline='') as p:
                writer = csv.writer(p)
                writer.writerows(temporary_data)
            print('Package Updated')
        else:
            print('Package Not Found')

    def delete(self):
        print('================== Delete Package ===============')
        self.show()
        target = input('Enter Package ID: ').upper()
        temporary_data = []
        found = False

        if not os.path.exists(self.filename):
            print('File Not Found')
            return

        with open(self.filename, 'r') as p:
            reader = csv.reader(p)
            for row in reader:
                if row and row[0] == target:
                    found = True
                    continue
                temporary_data.append(row)

        if found and input('Confirm Delete Package? y/n').lower() =='y':
            with open(self.filename, 'w', newline='') as p:
                writer = csv.writer(p)
                writer.writerows(temporary_data)
            print('Package Deleted')
        else:
            print('Package Not Found')







