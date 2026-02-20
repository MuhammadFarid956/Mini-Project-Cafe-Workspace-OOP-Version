import os
import csv

"""
super class (Entity)
Entity as a parent class
use inheritance concept (pewarisan)   
"""
class Entity:
    @staticmethod
    def gen_id(self, prefix):
        last_num = 0
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0].startswith(prefix):
                        try:
                            num = int(row[0].replace(prefix, '')) #Ambil angka setelah prefix
                            if num > last_num:
                                last_num = num
                        except ValueError:
                            continue
        return f"{prefix}{last_num + 1:03d}"