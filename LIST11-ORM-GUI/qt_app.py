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
from menu_bar import Menu_Bar
from output_data_widget import Output_Data_Widget


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DataBase()
        self._db_manip = DataBase_Manipulator( self.db )
        self._db_manip_add = Database_Manipulator_Add( self.db )
        self._db_manip_del = DataBase_Manipulator_Delete( self.db )
        self._init_UI()


    def _init_UI(self):
        self.left = 300
        self.top = 180
        self.width = 853
        self.height = 310
        self._up_margin = 30
        self._left_margin = 10


        # add Menu Bar
        self._menu_bar = Menu_Bar(["File", "Edit", "About"], self)
        # File
        self._menu_bar.add_separator_to_menu("File")
        self._menu_bar.add_menu_button("File", "Create DataBase Content", "Create the content of the DataBase", self._action_create_database_content)
        self._menu_bar.add_separator_to_menu("File")
        self._menu_bar.add_menu_button("File", "Exit", "Close Window", self.close)
        # Edit
        self._menu_bar.add_separator_to_menu("Edit")
        self._menu_bar.add_menu_button("Edit", "Load Persons", "Load persons to the table.", self._action_table_update_data_persons)
        self._menu_bar.add_menu_button("Edit", "Load Events", "Load events to the table.", self._action_table_update_data_events)
        self._menu_bar.add_separator_to_menu("Edit")
        self._menu_bar.add_menu_button("Edit", "Delete Persons", "Delete selected persons from the table.", self._action_delete_persons)
        self._menu_bar.add_menu_button("Edit", "Delete Events", "Delete selected events from the table.", self._action_delete_events)
        # About
        self._menu_bar.add_separator_to_menu("About")
        #self._menu_bar.add_menu_button("About", "Program", "Informations about the program.", self._show_info_program)
        #self._menu_bar.add_menu_button("About", "Author", "Informations about the program author.", self._show_info_author)
        

        # PERSONS
        # add buttons
        self._button_load_persons = Button(
            x=self._left_margin,
            y=self._up_margin,
            text="Load Persons",
            tooltip="Load persons to the table.",
            on_click=self._action_table_update_data_persons,
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
        # add table
        table_x = self._left_margin
        table_y = self._up_margin + self._button_load_persons.height()
        self._table_persons = Table(x=table_x, y=table_y, width=330, parent=self)
        self._delete_persons = Button(
            x=self._table_persons.x() + self._table_persons.width() - 119,
            y=self._table_persons.y() + self._table_persons.height() + 10,
            text="Delete Persons",
            tooltip="Delete persons selected on the table.",
            on_click=self._action_delete_persons,
            parent=self
        )


        # EVENTS
        # add buttons
        self._button_load_events = Button(
            x=self._table_persons.x() + self._table_persons.width() + 170,
            y=self._up_margin,
            text="Load Events",
            tooltip="Load persons to the table.",
            on_click=self._action_table_update_data_events,
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
        # add table
        table_x = self._button_load_events.x() 
        table_y = self._up_margin + self._button_load_persons.height()
        self._table_events = Table(x=table_x, y=table_y, width=330, parent=self)

        self._delete_events = Button(
            x=self._table_events.x() + self._table_events.width() - 119,
            y=self._table_events.y() + self._table_events.height() + 10,
            text="Delete Events",
            tooltip="Delete events selected on the table.",
            on_click=self._action_delete_events,
            parent=self
        )


        # OTHER
        # add buttons
        #self._button_init_db = Button(
        #    x=10,
        #    y=self._table_persons.y() + self._table_persons.height() + 10,
        #    text="Create DataBase",
        #    tooltip="You can create the DataBase content if it doesn't exists!",
        #    on_click=self._action_create_database_content,
        #    parent=self
        #)
        self._button_add_person_at_event = Button(
            x=self._left_margin + self._table_persons.x() + self._table_persons.width(),
            y=100,
            width=150,
            text="Add For Events",
            tooltip="Sign up the Persons for the Event.",
            on_click=self._action_add_person_at_event,
            parent=self
        )
        self._button_remove_person_at_event = Button(
            x=self._button_add_person_at_event.x(),
            y=self._button_add_person_at_event.y() + 85,
            width=150,
            text="Remove From Events",
            tooltip="Remove Persons from Events.",
            on_click=self._action_remove_persons_from_events,
            parent=self
        )
       
        # set window appearance
        self.setWindowTitle('Calendar Manager')
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()


    def _action_table_update_data_persons(self):
        self._table_persons.update_data(["id", "name", "email"], self.db.get_persons())


    def _action_table_update_data_events(self):
        self._table_events.update_data(["id", "title", "start time", "end time"], self.db.get_events())


    def _action_add_person(self):
        self._person_data_widget = Input_Person_Data_Widget(self._db_manip_add)
        self._action_table_update_data_persons()
        

    def _action_add_event(self):
        self._event_data_widget = Input_Event_Data_Widget(self._db_manip_add)
        self._action_table_update_data_events()

    def _action_add_person_at_event(self):
        persons_ids = self._table_persons.get_ids_of_selected()
        events_ids = self._table_events.get_ids_of_selected()
        if len(persons_ids) == 0 : 
                QMessageBox.about(self, "Create DataBase Content", "Select at least one person.")
        if len(events_ids) == 0 : 
                QMessageBox.about(self, "Create DataBase Content", "Select at least one event.")
        for person_id in persons_ids:
            for event_id in events_ids:
                message = self._db_manip_add.add_person_at_event({"person_id":person_id, "event_id":event_id})
                QMessageBox.about(self, "Create DataBase Content", message)


    def _action_create_database_content(self):
        message = self._db_manip.create_database_content()
        QMessageBox.about(self, "Create DataBase Content", message)


    def _action_delete_persons(self):
        for person_id in self._table_persons.get_ids_of_selected():
            message = self._db_manip_del.delete_person({"id":person_id})
            QMessageBox.about( self, "Delete Person", message )
        self._table_persons.remove_selected()


    def _action_delete_events(self):
        for event_id in self._table_events.get_ids_of_selected():
            message = self._db_manip_del.delete_event({"id":event_id})
            QMessageBox.about( self, "Delete Event", message )
        self._table_persons.remove_selected()

    def _action_remove_persons_from_events(self):
        self._output_data_widget = Output_Data_Widget(self.db)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())