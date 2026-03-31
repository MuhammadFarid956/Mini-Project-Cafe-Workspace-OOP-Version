class MenuUI:
    def __init__(self, menu_svc):
        self.menu_svc = menu_svc


    def show_menus(self):
        print('\n==================== List Menu ====================')
        menus = self.menu_svc.get_all()

        if not menus:
            print('Menu Empty')
            return
        else:
            print(f'{"ID":<5} | {"Menu":<20} | {"Price":>10}')
            print('='*41)
            for m in menus:
                print(f'{m.id:<5} | {m.name:<20} | Rp. {m.price:,}')

    def add_menu(self):
        print('\n==================== Add MenuService ====================')
        name = input('Name : ')

        try:
            price = int(input('Price : '))
            self.menu_svc.add(name, price)
            print('Successfully Added Menu')
        except ValueError:
            print('Invalid Input for price.')





# class CafeApp:
#     def __init__(self):
#         self.menu_mgr = MenuService()
#         self.package_mgr = PackageManager()
#         self.visitor = Visitor()
#         self.transaction = Transaction(self.menu_mgr, self.package_mgr, self.visitor)
#
#
#
#     def master_data(self):
#         try:
#             while True:
#
#
#                 if choice == "1":
#                     print("===== Master MenuService =====")
#                     print("1. Add Menu\n2. Show Menu\n3. Update Menu\n4. Delete Menu\n5. Back")
#                     choice = input("Enter your choice (1-5): ")
#                     if choice == "1": self.menu_mgr.add()
#                     elif choice == "2": self.menu_mgr.show()
#                     elif choice == "3": self.menu_mgr.update()
#                     elif choice == "4": self.menu_mgr.delete()
#                     elif choice == "5": continue
#                 elif choice == "2":
#                     print("===== Master Package =====")
#                     print("1. Add Package\n2. Show Package\n3. Update Package\n4. Delete Package\n5. Back")
#                     choice = input("Enter your choice (1-5): ")
#
#                     if choice == "1": self.package_mgr.add()
#                     elif choice == "2":self.package_mgr.show()
#                     elif choice == "3":self.package_mgr.update()
#                     elif choice == "4":self.package_mgr.delete()
#                     elif choice == "5": continue
#                 elif choice == "3":
#                     print("===== Master Visitor =====")
#                     print('1. Show Visitor\n2. Back')
#                     choice = input("Enter your choice (1-2): ")
#
#                     if choice == "1":self.visitor.show()
#                     elif choice == "2": continue
#                 elif choice == "4":
#                     return
#         except ValueError:
#             print("Invalid Choice")
#
#     def run(self):
#         while True:
#             print("===== Main MenuService =====")
#             print('1. Manager\n2. Transaction\n3. Exit')
#             choice = input("Enter your choice : ")
#
#
# if __name__ == '__main__':
#     app = CafeApp()
#     app.run()

