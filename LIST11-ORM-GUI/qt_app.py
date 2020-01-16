import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QAction

from db_manipulator import DataBase_Manipulator
from database_manipulator_add import Database_Manipulator_Add
from database_manipulator_delete import DataBase_Manipulator_Delete
from database import DataBase
from input_person_data_widget import Input_Person_Data_Widget
from input_event_data_widget import Input_Event_Data_Widget
from button import Button
from table import Table


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DataBase()
        self._db_manip = DataBase_Manipulator( self.db )
        self._db_manip_add = Database_Manipulator_Add( self.db )
        self._db_manip_del = DataBase_Manipulator_Delete( self.db )
        self.initUI()


    def initUI(self):
        self.left = 350
        self.top = 180
        self.width = 640
        self.height = 480
        self._up_margin = 30
        self._left_margin = 10


        # add buttons
        self._button_load_persons = Button(
            x=self._left_margin,
            y=self._up_margin,
            text="Load Persons",
            tooltip="Load persons to the table.",
            on_click=self._table_udate_data_persons,
            parent=self
        )
        self._button_add_person = Button(
            x=self._button_load_persons.x() + self._button_load_persons.width(), 
            y=self._up_margin, 
            width=30,
            text='+', 
            tooltip='You can add a new Person to the DataBase!', 
            on_click=self._action_add_person, 
            parent=self
        )
        self._button_load_events = Button(
            x=self._button_add_person.x() + self._button_add_person.width() + 20,
            y=self._up_margin,
            text="Load Events",
            tooltip="Load persons to the table.",
            on_click=self._table_udate_data_events,
            parent=self
        )
        self._button_add_event = Button(
            x=self._button_load_events.x() + self._button_load_events.width(),
            y=self._up_margin,
            width=30,
            text="+",
            tooltip="You can add a new Event to the Database!",
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
        self._delete_persons = Button(
            x=500,
            y=300,
            text="Delete Persons",
            tooltip="Delete persons selected on the table.",
            on_click=self._action_delete_persons,
            parent=self
        )

        # add table
        table_x = self._left_margin
        table_y = self._up_margin + self._button_load_persons.height()
        self._table = Table(x=table_x, y=table_y, parent=self)
       
        # set window appearance
        self.setWindowTitle('Calendar - PyQt5')
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()


    def _table_udate_data_persons(self):
        self._table.update_data(["id", "name", "email"], self.db.get_persons())


    def _table_udate_data_events(self):
        self._table.update_data(["id", "title", "start time", "end time"], self.db.get_events())



    def _action_add_person(self):
        self._person_data_widget = Input_Person_Data_Widget(self._db_manip_add)
        self._table_udate_data_persons()
        

    def _action_add_event(self):
        self._event_data_widget = Input_Event_Data_Widget(self._db_manip_add)
        self._table_udate_data_events()


    def _action_create_database_content(self):
        message = self.db_manip.create_database_content()
        QMessageBox.about(self, "Create DataBase Content", message)

    def _action_add_person_at_event(self):
        pass

    def _action_delete_persons(self):
        for item in self._table_person.selectedItems():

            person_id = int( self._table_person.item( item.row(), 0).text() )
            self._table_person.removeRow(item.row())

            QMessageBox.about(self, "Delete Person", self._db_manip_del.delete_person({"id":person_id}))


    def _action_delete_events(self):
        pass

    def _action_remove_persons_from_event(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())