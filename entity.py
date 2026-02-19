import os
import csv

"""
super class (Entity)
Entity as a parent class
use inheritance concept (pewarisan)   
"""
class Entity:
    def __init__(self, name):
        self.id = id
        self.name = name

    def gen_id(self, filename, prefix):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0].startswith(prefix):
                        try:
                            num = int(row[0].replace(prefix, ''))
                            if num > last_num:
                                last_num = num
                        except ValueError:
                            continue
        return f"{prefix}{last_num + 1:03d}"

    def name(self):
        return self.name