import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox

from db_manipulator import DataBase_Manipulator
from database_manipulator_add import Database_Manipulator_Add
from database_manipulator_delete import DataBase_Manipulator_Delete
from database import DataBase
from input_person_data_widget import Input_Person_Data_Widget


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        database = DataBase()
        self._db_manip = DataBase_Manipulator( database )
        self._db_manip_add = Database_Manipulator_Add( database )
        self._db_manip_del = DataBase_Manipulator_Delete( database )
        self.initUI()


    def initUI(self):
        self.left = 350
        self.top = 180
        self.width = 640
        self.height = 480

        # add buttons
        self._button_add_person = self._create_button(
            self._action_add_person, 
            name='Add Person', 
            tooltip='You can add a new person to the DataBase!'
        )
        self._button_add_event = self._create_button(
            self._action_add_event,
            x=300,
            name="Add Event",
            tooltip="You can add a new Person to the Database!"
        )
        self._button_init_db = self._create_button(
            self._action_create_database_content,
            x=200,
            name="Create DataBase",
            tooltip="You can create the DataBase content if it doesn't exists!"
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
        self._person_data_widget = Input_Person_Data_Widget(self._db_manip_add)
        

    def _action_add_event(self):
        self._event_data_widget = Input_Event_Data_Widget(self._db_manip_add)


    def _action_create_database_content(self):
        message = self.db_manip.create_database_content()
        QMessageBox.about(self, "Create DataBase Content", message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())