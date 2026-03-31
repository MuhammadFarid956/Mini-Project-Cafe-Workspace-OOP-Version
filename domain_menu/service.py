"""
Mengelola logika bisnis
"""
import datetime
from model import Menu
from core.base_service import BaseService
from core.base_repository import BaseRepository

class MenuService:
    def __init__(self, repository=BaseRepository ):
        self.repo = repository
        self._menus = self.repo.load_all()
        self._last_id = BaseService._calculate_last_id(self._menus, 'M')

    def get_by_id(self, m_id): return self._menus.get(m_id)
    def get_all(self): return self.menus.values()

    def add(self, name, price):
        self._last_id += 1
        new_id = f'M{self._last_id:03d}'
        new_menu = Menu(new_id, name, price)

        self._menus[new_id] = new_menu
        self.repo.save_all(self._menus)
        return new_menu

    def update(self, m_id, m_name=None, m_price=None):
        if m_id in self._menus:
            if m_name: self._menus[m_id].name = m_name
            if m_price: self._menus[m_id].price = int(m_price)
            self.repo.save_all(self._menus)
            return True
        return False

        # print('\n==================== Update Menu ====================')
        # self.show()
        # id_target = input('ID :').upper()

    def delete(self, m_id):
        # print('\n==================== Delete Menu ====================')
        # self.show()
        # id_target = input('ID :').upper()
        if m_id in self._menus:
           del self._menus[m_id]
           self.repo.save_all(self._menus)
           return True
        return False


