"""
Modul hanya berisi blueprint untuk objek
"""
class Menu:
    def __init__(self, m_id, m_name, m_price):
        self.id = m_id
        self.name = m_name
        self.price = m_price

    def to_csv_row(self):
        return [self.id, self.name, self.price]
