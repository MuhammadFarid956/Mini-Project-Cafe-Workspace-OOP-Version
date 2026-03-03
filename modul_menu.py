from entity import Entity
from master_data import MasterData
import csv

class Menu(Entity, MasterData):

    # filename = "menu_data.csv"
    def __init__(self, name=None, price=None):
        MasterData.__init__(self,"menu_data.csv", ["ID", "Menu", "Price"])#Constructor __init__
        self.filename = "menu_data.csv"
        self.prefix = "M"
        self.name = name
        self.price = price
        self.id = Entity.gen_id(self.filename, self.prefix)

    def add_menu(self):
        print("===== ADD MENU =====")
        id_menu = self.id
        self.name = input("Menu Name : ")
        self.price = int(input("Menu Price : "))

        with open("menu_data.csv", 'a', newline='' ) as file_menu:
            writer = csv.writer(file_menu)
            writer.writerow([id_menu, self.name, self.price])
        print("Success add menu")

    def show_menu(self):
        print("===== MENU =====")
        super().show()

    def update_price(self):
        print("===== UPDATE MENU =====")
        temporary_data = []
        self.show_menu()
        # target = None
        found = False
        target = input("Target ID : ")
        self.price = input("Menu Price : ").upper()

        try:
            with open(self.filename, 'r') as file_menu:
                reader = csv.reader(file_menu)
                for row in reader:
                    if row[0] == target:
                        print(f"Old Data : {row[1]} : Rp. {row[2]}")
                        print("Update Price : Rp.")
                        found = True
                    temporary_data.append(row)
        except FileNotFoundError:
            print("File not found")

        if found:
            with open(self.filename, 'w', newline='') as file_menu:
                writer = csv.writer(file_menu)
                writer.writerow(temporary_data)
            print("Success update price")
        else:
            print("ID not found")

    def delete_menu(self):
        print("===== DELETE MENU =====")
        target = input("ID Menu : ")
        self.delete(target)




t = Menu()
# t.add_menu()
# t.show_menu()
t.update_price()

# menu = Menu("Seblak", 100)
# menu.add_menu()
# print(menu.__dict__)

# tempilkan = Menu()
# tempilkan.show_menu()


