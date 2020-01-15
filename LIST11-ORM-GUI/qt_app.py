import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from db_manipulator import DataBase_Manipulator
from database import DataBase
from input_person_data_widget import Input_Person_Data_Widget

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_manip = DataBase_Manipulator( DataBase() )
        self.initUI()


    def initUI(self):
        self.left = 350
        self.top = 180
        self.width = 640
        self.height = 480
        self._button_add_person = self._create_button(
            self._action_add_person, 
            name='Add Person', 
            tooltip='You can add a new person to the database!'
        )
        self._button_init_db = self._create_button(
            self._create_database,
            x=200,
            name="Create DataBase",
            tooltip="You can create DataBase if it doesn't exists!"
        )
       
        self.setWindowTitle('Calendar - PyQt5')
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()


    def _create_button(self, action, name='', x=100, y=200, tooltip=''):
        button = QPushButton(name, self)
        button.setToolTip(tooltip)
        button.move(x, y)
        button.clicked.connect(action)
        return button
        

    def _action_add_person(self):
        self._person_data_widget = Input_Person_Data_Widget("person_data", self.db_manip)


    def _create_database(self):
        QMessageBox.about(self, "Message", str(self.db_manip.create_database()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())