from PyQt5.QtWidgets import QMenuBar, QAction

class Menu_Bar(QMenuBar):
    def __init__(self, menu_names, parent):
        super().__init__(parent=parent)
        self.parent = parent
        self.menu = {}
        for name in menu_names:
            self.menu[name] = self.addMenu(name)
            
         
    def add_menu_button(self, menu_name, text, status_tip, trigger):
        but = QAction(text, self.parent)
        but.setStatusTip(status_tip)
        but.triggered.connect(trigger)
        self.menu[menu_name].addAction(but)
        

    def add_separator_to_menu(self, name):
        sep = self.menu[name].addSeparator()


    def get_menu(self, name):
        return self.menu[name]