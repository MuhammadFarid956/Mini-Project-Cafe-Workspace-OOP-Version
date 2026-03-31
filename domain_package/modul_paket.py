import csv
import os

class PackageManager:
    def __init__(self, filename='paket_data.csv'):
        self.filename = filename
        self.packages = {}
        self.last_id = 0
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        p_id = row[0]
                        self.packages[p_id] = {
                            'name' : row[1], 'type' : row[2],
                            'min_order' : int(row[3]), 'capacity' : int(row[4]),
                            'duration' : int(row[5]), 'price' : int(row[6])
                        }
                        num = int(p_id.replace('P', ''))
                        if num > self.last_id:
                            self.last_id = num

    def next_id(self):
        self.last_id += 1
        return f'P{self.last_id:03d}'

    def save_data(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for p_id, data in self.packages.items():
                writer.writerow([p_id, data['name'], data['type'], data['min_order'], data['capacity'], data['duration'], data['price']])

    def show(self):
        print('================= Package =================')
        if not self.packages:
            print('Package Not Found')
            return

        print(f'{"ID":<5} | {"Name":<20} | {"Type":<10} | {"Min Order/Person":<20} | {"Price":>12}')
        print('='*80)
        for p_id, data in self.packages.items():
            print(f'{p_id:<5} | {data["name"]:<20} | {data["type"]:<10} | {data["min_order"]:<16} | {data["price"]:>12}')

    def add(self):
        print('================= Add Package =================')
        id_package = self.next_id()
        name = input('Enter Package Name: ')
        type_pack = input('Enter Package Type: ')
        min_order = int(input('Enter Package Min Order/Person: '))
        capacity = int(input('Enter Package Capacity: '))
        duration = int(input('Enter Package Duration: '))
        price = int(input('Enter Package Price: '))

        self.packages[id_package] = {
            'name' : name, 'type' : type_pack,
            'min_order' : min_order, 'capacity' : capacity,
            'duration' : duration, 'price' : price
        }
        self.save_data()
        print('Package Added')

    def update(self):
        print('================== Update Package =================')
        self.show()
        id_target =input('Enter Package ID: ').upper()

        if id_target in self.packages:
            package = self.packages[id_target]
            print(f'================= Package Information =================')
            print(f'Name : {package["name"]}\nType : {package["type"]}\nMin Order/Person : {package["min_order"]}\nCapacity : {package["capacity"]}\nDuration : {package["duration"]}\nPrice : {package["price"]}')

            new_min_order = input('Enter Package Min Order/Person (Click Enter to Continue): ')
            new_capacity = input('Enter Package Capacity (Click Enter to Continue): ')
            new_duration = input('Enter Package Duration (Click Enter to Continue): ')
            new_price = input('Enter Package Price (Click Enter to Continue): ')

            if new_min_order:
                self.packages[id_target] = int(new_min_order)
            if new_capacity:
                self.packages[id_target] = int(new_capacity)
            if new_duration:
                self.packages[id_target] = int(new_duration)
            if new_price:
                self.packages[id_target] = int(new_price)
            self.save_data()
            print('Package Updated')
        else:
            print('Package Not Found')

    def delete(self):
        print('================== Delete Package ===============')
        self.show()
        target = input('Enter Package ID: ').upper()
        if target in self.packages:
            if input('Do you want to delete this package? (y/n): ').lower() == 'y':
                del self.packages[target]
                self.save_data()
                print('Package Deleted')
        else:
            print('Package Not Found')