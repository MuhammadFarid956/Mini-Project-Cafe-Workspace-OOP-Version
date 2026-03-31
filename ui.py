from modul_menu import MenuManager
from modul_paket import PackageManager
from modul_visitor import Visitor
from transaction import Transaction

class CafeApp:
    def __init__(self):
        self.menu_mgr = MenuManager()
        self.package_mgr = PackageManager()
        self.visitor = Visitor()
        self.transaction = Transaction(self.menu_mgr, self.package_mgr, self.visitor)



    def master_data(self):
        try:
            while True:
                print("===== Master Data =====")
                print("1. MenuManager\n2. Package\n3. Visitor\n4. Back")
                choice = input("Enter your choice : ")

                if choice == "1":
                    print("===== Master MenuManager =====")
                    print("1. Add Menu\n2. Show Menu\n3. Update Menu\n4. Delete Menu\n5. Back")
                    choice = input("Enter your choice (1-5): ")
                    if choice == "1": self.menu_mgr.add()
                    elif choice == "2": self.menu_mgr.show()
                    elif choice == "3": self.menu_mgr.update()
                    elif choice == "4": self.menu_mgr.delete()
                    elif choice == "5": continue
                elif choice == "2":
                    print("===== Master Package =====")
                    print("1. Add Package\n2. Show Package\n3. Update Package\n4. Delete Package\n5. Back")
                    choice = input("Enter your choice (1-5): ")

                    if choice == "1": self.package_mgr.add()
                    elif choice == "2":self.package_mgr.show()
                    elif choice == "3":self.package_mgr.update()
                    elif choice == "4":self.package_mgr.delete()
                    elif choice == "5": continue
                elif choice == "3":
                    print("===== Master Visitor =====")
                    print('1. Show Visitor\n2. Back')
                    choice = input("Enter your choice (1-2): ")

                    if choice == "1":self.visitor.show()
                    elif choice == "2": continue
                elif choice == "4":
                    return
        except ValueError:
            print("Invalid Choice")

    def run(self):
        while True:
            print("===== Main MenuManager =====")
            print('1. Manager\n2. Transaction\n3. Exit')
            choice = input("Enter your choice : ")

            if choice == "1":
                self.master_data()
            elif choice == "2":
                print('=========================== Transaction ===========================')
                print('1. Cashier\n2. Transaction Report\n3. Back')
                choice = input("Enter your choice : ")

                if choice == "1":
                    self.transaction.transaction_process()
                elif choice == "2":
                    self.transaction.show()
            elif choice == "3":
                print('Thank You, Good Bye!')
                break
            else:
                print("Invalid Choice: Please Input (1/2/3)")

if __name__ == '__main__':
    app = CafeApp()
    app.run()

