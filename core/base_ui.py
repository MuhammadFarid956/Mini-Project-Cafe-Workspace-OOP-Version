class ConsoleUI:
    def prompt_enter(self): input('\nPress enter to continue...')

class MasterDataUI(ConsoleUI):
    def __init__(self, menu_svc, package_svc, visitor_svc):
        self.menu_svc = menu_svc
        self.package_svc = package_svc
        self.visitor_svc = visitor_svc
