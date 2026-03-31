import csv
import datetime
import os

class Transaction:
    def __init__(self, menu_mgr, package_mgr, visitor_mgr, filename='transactions_data.csv'):
        self.filename = filename
        self.menu_mgr = menu_mgr
        self.pack_mgr = package_mgr
        self.vst_mgr = visitor_mgr

    def show(self):
        print('\n================================ Transaction Details ==========================')
        if not os.path.exists(self.filename):
            print(f'Transaction Details file {self.filename} does not exist. Please create it.')
            return
        with open(self.filename, 'r') as e:
            reader = csv.reader(e)
            print(f'{"ID":<14} | {"Date":<11} | {"ID Visitor":<6} | {"ID Package":<5} | {"Total":>7}')
            print('-'*80)
            for row in reader:
                if row:
                    print(f'{row[0]:<14} | {row[1]:<11} | {row[2]:<10} | {row[3]:<10} | Rp {int(row[7]):,}')
            print('-' * 80)
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

            #Pengecekan data langsung dari RAM (O(0)) tanpa buka file CSV!
            if id_package not in self.pack_mgr.packages:
                return print('Package Not Found')

            package = self.pack_mgr.packages[id_package]
            num_person = int(input('Enter Number of Person: '))

            type_package = package['type']
            total= 0
            item_menu = ''

            if type_package == 'Non Rent':
                min_total = package['min_order'] * num_person
                self.menu_mgr.show()
                print(f'Minimum Order : {min_total:,}')

                items = input('Enter the number of items (pisah dengan tanda koma): ').strip().upper()
                item_ids = [x.strip() for x in items.split(',') if x.strip()]
                item_menu = ';'.join(item_ids)

                for mid in item_ids:
                    if mid in self.menu_mgr.menus:
                        total += self.menu_mgr.menus[mid]['price']
                    else:
                        print('Menu Not Found')

                if total < min_total:
                    return print(f'Total Order = {total:,}, les than  Minimum Order : {min_total:,}')

            else:
                total = int(package['price']) * num_person

            with open(self.filename, 'a', newline='') as e:
                writer = csv.writer(e)
                writer.writerow([id_transaction, date_transaction, id_vst, id_package, type_package, num_person, item_menu, total])

            print('===================== Transaction Details =======================')
            print(f'ID Transaction : {id_transaction}\nDate : {date_transaction}')
            print('-'*80)
            print('Transaction Process Complete')
        except ValueError:
            print(f'Input Invalid. Please try again.')




