import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox

from db_manipulator import DataBase_Manipulator
from database_manipulator_add import Database_Manipulator_Add
from database_manipulator_delete import DataBase_Manipulator_Delete
from database import DataBase
from input_person_data_widget import Input_Person_Data_Widget
from input_event_data_widget import Input_Event_Data_Widget
from button import Button


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
        self._button_add_person = Button(
            x=100, 
            y=200, 
            text='Add Person', 
            tooltip='You can add a new person to the DataBase!', 
            on_click=self._action_add_person, 
            parent=self
        )
        self._button_add_event = Button(
            x=220,
            y=200,
            text="Add Event",
            tooltip="You can add a new Person to the Database!",
            on_click=self._action_add_event,
            parent=self
        )
        self._button_init_db = Button(
            x=340,
            y=200,
            text="Create DataBase",
            tooltip="You can create the DataBase content if it doesn't exists!",
            on_click=self._action_create_database_content,
            parent=self
        )
       
        self.setWindowTitle('Calendar - PyQt5')
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()


    def _action_add_person(self):
        self._person_data_widget = Input_Person_Data_Widget(self._db_manip_add)
        

    def _action_add_event(self):
        self._event_data_widget = Input_Event_Data_Widget(self._db_manip_add)


    def _action_create_database_content(self):
        message = self.db_manip.create_database_content()
        QMessageBox.about(self, "Create DataBase Content", message)

    def _action_add_person_at_event(self):
        pass

    def _action_delete_persons(self):
        pass

    def _action_delete_events(self):
        pass

    def _action_remove_persons_from_event(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())