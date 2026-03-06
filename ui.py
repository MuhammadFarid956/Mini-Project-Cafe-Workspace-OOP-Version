# from io import Input
from modul_menu import Menu
from modul_paket import PackageManager



class CafeApp:
    def __init__(self):
        self.menu_mgr = Menu()
        self.package_mgr = PackageManager()

    def master_data(self):
        try:
            while True:
                print("===== Master Data =====")
                print("1. Menu\n2. Package\n3. Visitor\n4. Back")
                choice = input("Enter your choice : ")

                if choice == "1":
                    if choice == "1":
                        print("===== Master Menu =====")
                        print("1. Add Menu\n2. Show Menu\n3. Update Menu\n4. Delete Menu\n5. Back")
                        choice = input("Enter your choice : ")
                        if choice == "1": self.menu_mgr.add()
                        elif choice == "2": self.menu_mgr.show()
                        elif choice == "3": self.menu_mgr.update()
                        elif choice == "4": self.menu_mgr.delete()
                elif choice == "2":
                    print("===== Master Package =====")
                    print("1. Add Package\n2. Show Package\n3. Update Package\n4. Delete Package\n5. Back")
                    choice = input("Enter your choice : ")
                    if choice == "1":
                        self.package_mgr.add()
                    elif choice == "2":
                        self.package_mgr.show()
                    elif choice == "3":
                        self.package_mgr.update()
                    elif choice == "4":
                        self.package_mgr.delete()
        except ValueError:
            print("Invalid Choice")


if __name__ == '__main__':
    app = CafeApp()
    app.master_data()

