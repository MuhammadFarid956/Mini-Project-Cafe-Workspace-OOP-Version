import csv
import os

class Visitor:
    def __init__(self, filename='visitors_data.csv'):
        self.filename = filename

    def nex_id(self):
        last_num = 0
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as e:
                reader = csv.reader(e)
                for row in reader:
                    if row and row[0].startswith('V'):
                        num = int(row[0].replace('V', ''))
                        if last_num > num: last_num = num
        return f'{last_num + 1:03d}'

    def show(self):
        print('=================== Visitor Info =====================')
        if not os.path.exists(self.filename):
            print(f'File {self.filename} does not exist')
            return
        with open(self.filename, 'r') as e:
            reader = csv.reader(e)
            print(f'{"ID":<5} | {"Name":<20} | {"No HP":<12} | {"Instance":<20}')
            for row in reader:
                if row:
                    print(f'{row[0]:<5} {row[1]:<20} {row[2]:<12} | {row[3]:<20}')

    def add(self):
        print('=================== Add Visitor ======================')
        id_vst = self.nex_id()
        name = input('Enter Visitor Name: ')
        no_hp = input('Enter Visitor No HP: ')
        instance = input('Enter Visitor Instance: ')

        with open(self.filename, 'a', newline='') as e:
            writer = csv.writer(e)
            writer.writerow([id_vst, name, no_hp, instance])
        print('Visitor Info Added')
        return id_vst

    def delete(self):
        print('=================== Delete Visitor ====================')
        self.show()
        target =input('Enter ID Target : ')
        temporary_data = []
        found = False
        with open(self.filename, 'r') as e:
            reader = csv.reader(e)
            for row in reader:
                if row and row[0] == target:
                    found = True
                    continue
                temporary_data.append(row)

        if found and input('Confirm Delete Visitor? (y/n): ').lower() == 'y':
            with open(self.filename, 'w') as e:
                writer = csv.writer(e)
                writer.writerows(temporary_data)
            print('Visitor Info Deleted')
        elif not found:
            print('Visitor Info Not Found')

