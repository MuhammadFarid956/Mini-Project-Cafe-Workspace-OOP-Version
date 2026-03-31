from  domain_menu.repository import MenuRepository

from domain_menu.service import MenuService

from domain_menu.ui import MenuUI

class CafeApp:
    def __init__(self):
        #   1. Inisisalisasi Repositories (Layer Database/File)
        menu_repo = MenuRepository('menu_data.csv')

        #   2. Inisialisasi Services (Layer Logika) - Inject Repositories
        self.menu_svc = MenuService(menu_repo)

        #   3. Transaction butuh akses ke service lain untuk validasi


    def run(self):
        while True:
            print("===== Cafe Workspace App =====")
            print("1. Master Data\n2. Transaction\n3. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.run_master_data()
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

    def run_master_data(self):

