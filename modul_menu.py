from fileinput import filename

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
        print("[ ADD MENU ]")
        id_menu = self.id

        with open("menu_data.csv", 'a', newline='' ) as file_menu:
            writer = csv.writer(file_menu)
            writer.writerow([id_menu, self.name, self.price])
        print("Success add menu")

    def show_menu(self):
        print("[ MENU ]")
        super().show()

# menu = Menu("Seblak", 100)
# menu.add_menu()
# print(menu.__dict__)

tempilkan = Menu()
tempilkan.show_menu()


