import csv
import os

class MenuManager:
    def __init__(self, filename='menu_data.csv'):
        self.filename = filename
        self.menus = {} #In-Memory Data Structure (Dictionary)
        self.last_id = 0
        self.load_data() #Muat data sekali di awal

    def load_data(self):
        """Membaca file CSV satu kali dan menyimpannya di memory (Dictionary)."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        m_id, name, price = row[0], row[1], int(row[2])
                        self.menus[m_id] = {'name': name, 'price': price}
                        #Lacak ID terakhir agar tidak perlu looping lagi
                        num = int(m_id.replace('M', ''))
                        if num > self.last_id:
                            self.last_id = num

    def save_data(self):
        """Menyimpan seluruh isi Dictionary kembali ke CSV (Dipanggil hanya saat ada perubahan"""
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for m_id, data in self.menus.items():
                writer.writerow([m_id, data['name'], data['price']])

    def next_id(self):
        """Membuat ID baru tanpa perlu membaca file CSV (O(1))."""
        self.last_id = self.last_id + 1
        return f'M{self.last_id:03d}'

    def show(self):
        print('\n==================== List Menu ====================')
        if not self.menus:
            print('Menu Empty')
            return

        print(f'{"ID":<5} | {"Menu":<20} | {"Price":>10}')
        print('='*41)
        for m_id, data in self.menus.items():
            print(f'{m_id:<5} | {data["name"]:<20} | Rp. {data["price"]:,}')

    def add(self):
        print('\n==================== Add MenuManager ====================')
        id_menu = self.next_id()
        name = input('Name : ')
        price = int(input('Price :'))

        #Simpan ke memory dn langsung simpan ke file
        self.menus[id_menu] = {'name': name, 'price': price}
        self.save_data()
        print('Successfully Added MenuManager')

    def update(self):
        print('\n==================== Update Menu ====================')
        self.show()
        id_target = input('ID :').upper()

        #Cek ketersediaan data langsung di RAM (O(1))
        if id_target in self.menus:
            menu = self.menus[id_target]
            print(f'Menu : {menu["name"]}\nPrice : {menu["price"]} ')
            new_name = input('Name (Click Enter to Continue) : ')
            new_price = input('Price (Click Enter to Continue):')

            if new_name:
                self.menus[id_target]['name'] = new_name
            if new_name:
                self.menus[id_target]['price'] = int(new_price)

            self.save_data()
            print('Successfully Updated Menu')
        else:
            print('ID Menu not found')

    def delete(self):
        print('\n==================== Delete Menu ====================')
        self.show()
        id_target = input('ID :').upper()
        if id_target in self.menus:
            del self.menus[id_target] #Hapus dari RAM (Sangat Cepat)
            self.save_data()  # Update isi file CSV
            print('Successfully Deleted')
        else:
            print('ID Menu Not Found')


