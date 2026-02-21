

from modul_menu import Menu

# Modul Menu
class Input(Menu):

    @staticmethod
    def inp_add():
        name = input("Menu Name : ")
        price = int(input("Menu Price : "))
        menu = Menu()
        menu.add_menu()

    @staticmethod
    def inp_price():
        price = int(input("Menu Price : "))
        menu = Menu(price)
        menu.update_price()

    @staticmethod
    def inp_delete():
        target = input("ID Menu : ")
        menu = Menu()
        menu.delete(target)




