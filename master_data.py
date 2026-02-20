import os
import csv
"""
use polymorphism concept (banyak object)
merujuk pada object/method/fungsi dengan nama yang sama yang dapat dieksekusi pada banyak object/class
"""
class MasterData:
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers

    def show(self):
        if not os.path.exists(filename):
            print("Empty Data File")
            return

        with open(filename, 'r') as file:
            reader = csv.reader(file)
            # Menampilkan header secara dinamis
            format_header = "|".join([f"h:<15" for h in self.headers])
            print(format_header)
            print("-"* len(format_header))

            for row in reader:
                print("|".join([f"{item:<15}" for item in row]))

    def delete(self, target):
        self.show()

        temporary_data = []
        found = False
        if not os.path.exists(self.filename):
            print("File Not Found")

        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].upper() == target.upper():
                    found = True
                    continue
                temporary_data.append(row)

        if found:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(temporary_data)


