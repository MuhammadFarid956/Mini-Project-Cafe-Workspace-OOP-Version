from io import Input
from modul_menu import Menu


class Interface:
    @staticmethod
    def menu():
        while True:
            print("===== Cafe Workspace OOP Version =====")
            print("1. Manager")
            print("2. Transaction")
            print("3. Exit")
            choice = input("Enter your choice : ")

            if choice == "1":
                while True:
                    print("===== Manager Menu =====")
                    print("1. Menu Cafe Workspace")
                    print("2. Paket Cafe Workspace")
                    print("3. Visitor Cafe Workspace")
                    print("4. Back")
                    choice = input("Enter your choice : ")
                    if choice == "1":
                        print("===== Menu Manager =====")
                        print("1. Add Menu\n2. Show Menu\n3. Update Menu\n4. Delete Menu\n5. Delete Menu\n6. Exit")
                        choice = input("Enter your choice : ")
                        if choice == "1":
                            add = Input()
                            add.inp_add()
                        elif choice == "2":
                            show = Menu()
                            show.show_menu()
                        elif choice == "3":
                            upd = Input()
                            upd.inp_price()
                        elif choice == "4":
                            dele = Input()
                            dele.inp_delete()
                        elif choice == "5":
                            continue
                        else:
                            print("Invalid Choice")

if __name__ == '__main__':
    run = Interface()
    run.menu()

