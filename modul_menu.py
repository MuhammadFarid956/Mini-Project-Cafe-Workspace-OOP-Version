# from entity import Entity
# from master_data import MasterData
# import csv
#
# class Menu(Entity, MasterData):
#
#     def __init__(self, name=None, price=None):
#         MasterData.__init__(self,"menu_data.csv", ["ID", "Menu", "Price"])#Constructor __init__
#         self.filename = "menu_data.csv"
#         self.prefix = "M"
#         self.name = name
#         self.price = price
#         self.id = Entity.gen_id(self.filename, self.prefix)
#
#     def add_menu(self):
#         print("===== ADD MENU =====")
#         id_menu = self.id
#         self.name = input("Menu Name : ")
#         self.price = int(input("Menu Price : "))
#
#         with open("menu_data.csv", 'a', newline='' ) as file_menu:
#             writer = csv.writer(file_menu)
#             writer.writerow([id_menu, self.name, self.price])
#         print("Success add menu")
#
#     def show_menu(self):
#         print("===== MENU =====")
#         super().show()
#
#     def update_price(self):
#         print("===== UPDATE MENU =====")
#         temporary_data = []
#         self.show_menu()
#         # target = None
#         found = False
#         target = input("Target ID : ")
#         new_price = input("Menu Price : ").upper()
#
#         try:
#             with open(self.filename, 'r') as file_menu:
#                 reader = csv.reader(file_menu)
#                 for row in reader:
#                     if row[0] == target:
#                         print(f"Old Data : {row[1]} : Rp. {row[2]}")
#                         row[2] = new_price
#                         print(f"Update Price : Rp. {row[2]}")
#                         found = True
#                     temporary_data.append(row)
#         except FileNotFoundError:
#             print("File not found")
#
#         if found:
#             with open(self.filename, 'w', newline='') as file_menu:
#                 writer = csv.writer(file_menu)
#                 writer.writerows(temporary_data)
#             print("Success update price")
#         else:
#             print("ID not found")
#
#     def delete_menu(self):
#         print("===== DELETE MENU =====")
#         target = input("ID Menu : ")
#         self.delete(target)
#
import csv
import os

class Menu:
    def __init__(self, filename='menu_data.csv'):
        self.filename = filename

    def next_id(self):
        last_num = 0
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as menu_file:
                reader = csv.reader(menu_file)
                for row in reader:
                    if row and row[0].startswith('M'):
                        num = int(row[0].replace('M', ''))
                        if num > last_num:
                            last_num = num
        return f'M{last_num+1:03d}'

    def show(self):
        print('\n==================== List Menu ====================')
        if not os.path.exists(self.filename):
            print('Menu Empty')
            return
        with open(self.filename, 'r') as menu_file:
            reader = csv.reader(menu_file)
            print(f'{"ID":<5} | {"Menu":<20} | {"Price":>10}')
            print('='*41)
            for row in reader:
                if row:
                    print(f'{row[0]:<5} | {row[1]:<20} | ${int(row[2]):,}')

    def add(self):
        print('\n==================== Add Menu ====================')
        id_menu = self.next_id()
        name = input('Name : ')
        price = int(input('Price :'))

        with open(self.filename, 'a', newline='') as menu_file:
            writer = csv.writer(menu_file)
            writer.writerow([id_menu, name, price])
        print('Successfully Added Menu')

    def update(self):
        print('\n==================== Update Menu ====================')
        self.show()
        id_target = input('ID :').upper()
        temporary_data = []

        if not os.path.exists(self.filename):
            print('File not found')
            return
        found = False

        with open(self.filename, 'r') as menu_file:
            reader = csv.reader(menu_file)
            for row in reader:
                if row and row[0] == id_target:
                    print(f'Menu : {row[1]}\nPrice : {row[2]} ')
                    new_name = input('Name (Click Enter to Continue) : ')
                    new_price = input('Price (Click Enter to Continue):')

                    if len(new_name) > 0:
                        row[1] = new_name
                    if len(new_price) > 0:
                        row[2] = new_price

                    found = True
                    print('Process Updated')
                temporary_data.append(row)

        if found:
            with open(self.filename, 'w', newline='') as menu_file:
                writer = csv.writer(menu_file)
                writer.writerows(temporary_data)
            print('Successfully Updated Menu')
        else:
            print('ID Menu Not Found')

    def delete(self):
        print('\n==================== Delete Menu ====================')
        self.show()
        id_target = input('ID :').upper()
        temporary_data = []
        found = False

        if not os.path.exists(self.filename):
            print('File not found')
            return

        with open(self.filename, 'r') as menu_file:
            reader = csv.reader(menu_file)
            for row in reader:
                if row and row[0] == id_target:
                    found = True
                    continue
                temporary_data.append(row)

        if found:
            confirm = input('Are you sure you want to delete the menu ? (y/n) : ')
            if confirm == 'y':
                with open(self.filename, 'w', newline='') as menu_file:
                    writer = csv.writer(menu_file)
                    writer.writerows(temporary_data)
                print('Successfully Deleted Menu')
            else:
                print('ID Menu Not Found')
        else:
            print('ID Menu Not Found')



