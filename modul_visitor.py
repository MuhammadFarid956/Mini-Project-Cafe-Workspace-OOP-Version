import csv
import os

class Visitor:
    def __init__(self, filename='visitors_data.csv'):
        self.filename = filename
        self.visitors = {}
        self.last_id = 0
        self.load_data()

    def load_data(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    v_id = row[0]
                    self.visitors[v_id] = {'name': row[1], 'no_hp': row[2], 'instance': row[3]}
                    num = int(v_id.replace('V', ''))
                    if num > self.last_id:
                        self.last_id = num

    def nex_id(self):
        self.last_id += 1
        return f'V{self.last_id:03d}'

    def save_data(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for v_id, data in self.visitors.items():
                writer.writerow([v_id, data['name'], data['no_hp'], data['instance']])

    def show(self):
        print('=================== Visitor Info =====================')
        print(f'{"ID":<5} | {"Name":<20} | {"No HP":<12} | {"Instance":<20}')
        for v_id, data in self.visitors.items():
            print(f'{v_id:<5} | {data["name"]:<20} | {data["no_hp"]:<12} | {data["instance"]:<20}')

    def add(self):
        print('=================== Add Visitor ======================')
        id_vst = self.nex_id()
        name = input('Enter Visitor Name: ')
        no_hp = input('Enter Visitor No HP: ')
        instance = input('Enter Visitor Instance: ')

        self.visitors[id_vst] = {'name': name, 'no_hp': no_hp, 'instance': instance}
        self.save_data()
        print('Visitor Info Added')
        return id_vst #Mengembalikan ID untuk digunakan di transaksi
