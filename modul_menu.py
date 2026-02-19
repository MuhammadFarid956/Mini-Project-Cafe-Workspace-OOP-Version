from entity import Entity
from master_data import MasterData

class Menu(Entity):
    def __init__(self, id_menu, price):
        super().__init__(id)
        self.id_menu = id_menu if id_menu else self.gen_id('menu_data.csv', 'M')
        self.price = price


    def show_menu(self):
        MasterData.show("menu_data.csv")

