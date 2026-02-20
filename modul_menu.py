from entity import Entity
import csv

class Menu(Entity):

    # filename = "menu_data.csv"
    def __init__(self, name, price): #Constructor __init__
        super().__init__()
        self.name = name
        self.price = price

    def add_menu(self):
        print("[ ADD MENU ]")
        id_menu = self.gen_id(self, "M")

        with open("menu_data.csv", 'a', newline='' ) as file_menu:
            writer = csv.writer(file_menu)
            writer.writerows([id_menu, self.name, self.price])
        print("Success add menu")

menu = Menu("Seblak", 100)
menu.add_menu()
print(menu)

