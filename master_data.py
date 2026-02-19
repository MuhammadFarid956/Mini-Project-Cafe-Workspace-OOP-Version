import os
import csv
from os import write

"""
use polymorphism concept (banyak object)
merujuk pada object/method/fungsi dengan nama yang sama yang dapat dieksekusi pada banyak object/class
"""
class MasterData:
    def show(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        return filename

    def delete(self, filename, target):
        self.show(filename)

        temporary_data = []
        found = False
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row == target:
                        found = True
                        continue
                    temporary_data.append(row)

        if found:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(temporary_data)


