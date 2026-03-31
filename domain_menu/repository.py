import csv, os
from model import Menu #Import dari folder yang sama

class MenuRepository:
    def __init__(self, filename='menu_data.csv'):
        self.filename = filename

    def load_all(self):
        menus = {}
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        menus[row[0]] = Menu(row[0], row[1], int(row[2]))
        return menus

    def save_all(self, menus_dict):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for menu_obj in menus_dict.values():
                writer.writerow(menu_obj.to_csv_row())

