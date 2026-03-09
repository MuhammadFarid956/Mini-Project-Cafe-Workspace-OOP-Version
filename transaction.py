import csv
import datetime
import os

class Transaction:
    def __init__(self, menu_mgr, package_mgr, visitor_mgr, filename='transactions_data.csv'):
        self.filename = filename
        self.menu_mgr = menu_mgr
        self.pack_mgr = package_mgr
        self.vst_mgr = visitor_mgr

    def loockup_package(self, id_package):
        if not os.path.exists(self.pack_mgr.filename):
            return None
        with open(self.pack_mgr.filename, 'r') as p:
            reader =  csv.reader(p)
            for row in reader:
                if row and row[0] == id_package:
                    return row
        return None

    def loockup_menu(self, id_menu):
        if not os.path.exists(self.menu_mgr.filename):
            return 0
        with open(self.menu_mgr.filename, 'r') as e:
            reader = csv.reader(e)
            for row in reader:
                if row and row[0] == id_menu:
                    return int(row[2])
        return 0

    def show(self):
        print('\n================================ Transaction Details ==========================')
        if not os.path.exists(self.filename):
            print(f'Transaction Details file {self.filename} does not exist. Please create it.')
            return
        with open(self.filename, 'r') as e:
            reader = csv.reader(e)
            print(f'{"ID":<14} | {"Date":<11} | {"ID Visitor":<6} | {"ID Package":<5} | {"Type":<9} | {"num":<2} | {"Items":<20} |Rp {"total":>7}')
            print('-'*120)
            for row in reader:
                if row:
                    print(f'{row[0]:<14} | {row[1]:<11} | {row[2]:<10} | {row[3]:<10} | {row[4]:<9} | {row[5]:<3} | {row[6]:<20} | {row[7]:>7}')

    def receipt_trc(self):
        print('\n=============================== Transaction Details ==========================')
        if not os.path.exists(self.filename):
            print()
    def transaction_process(self):
        try:
            id_transaction = datetime.datetime.now().strftime('T%y%m%d%H%M%S')
            date_transaction = datetime.date.today().isoformat()

            id_vst = self.vst_mgr.add() #Call function add() from instance class Visitor

            self.pack_mgr.show()
            id_package = input('Enter ID Package: ').upper()
            num_person = int(input('Enter Number of Person: '))

            package = self.loockup_package(id_package)
            if not package:
                return print('No package found')
            type_package = package[2]
            total= 0
            item_menu = ''

            if type_package == 'Non Rent':
                min_order_per_person = int(package[3])
                min_total = min_order_per_person * num_person
                self.menu_mgr.show()
                print(f'Minimum Order : {min_total:,}')
                items = input('Enter the number of items (pisah dengan tanda koma): ').strip().upper()
                item_ids = [x.strip() for x in items.split(',') if x.strip()]
                item_menu = ';'.join(item_ids)

                for mid in item_ids:
                    total += self.loockup_menu(mid)
                if total < min_total:
                    return print(f'Total Order = {total:,}, les than  Minimum Order : {min_total:,}')

            else:
                total = int(package[6]) * num_person

            with open(self.filename, 'a', newline='') as e:
                writer = csv.writer(e)
                writer.writerow([id_transaction, date_transaction, id_vst, id_package, type_package, num_person, item_menu, total])
                print('===================== Transaction Details =======================')
                print(f'ID Transaction : {id_transaction}\nDate : {date_transaction}')
                print('-'*120)
                for row

            print('Transaction Process Complete')
        except ValueError:
            print(f'Input Invalid. Please try again.')




