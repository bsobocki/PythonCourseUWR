from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QLabel, QMessageBox

from table import Table
from database_manipulator_delete import DataBase_Manipulator_Delete
from button import Button

class Output_Data_Widget(QWidget):
    def __init__(self, database):
        super().__init__()
        self._db = database
        self._db_manip_del = DataBase_Manipulator_Delete(self._db)

        self.setWindowTitle("Remove Persons From Selected Event")

        # Events
        self._label_events = QLabel("Events",self)
        self._label_events.move(
            10, 
            10
        )
        self._table_events = Table(
            x=10, 
            y=self._label_events.y() + self._label_events.height(), 
            width=330, 
            parent=self
        )
        self._table_events.update_data(["title", "start","end"],self._db.get_events())

        # Persons
        self._label_persons = QLabel("Persons", self)
        self._label_persons.move(
            self._table_events.x() + self._table_events.width() + 10, 
            10
        )
        self._table_persons = Table(
            x=self._label_persons.x(),
            y=self._label_persons.y() + self._label_persons.height(),
            width=330,
            parent=self
        )

        # Button
        self._button_remove = Button(
            x=self._table_persons.x() + self._table_persons.width() - 118,
            y=self._table_persons.y() + self._table_persons.height() + 10,
            text="Remove",
            tooltip="Remove the selected Persons from the selected event.",
            on_click=self._action_delete_person_from_event,
            parent=self
        )

        self.show()
        

    def _action_delete_person_from_event(self):
        selected_events_ids = self._table_events.get_ids_of_selected()
        for selected_id in selected_events_ids:
            rows_ids = [x[0] for x in self._db.get_persons_at_event(selected_id)]
            message = self._db_manip_del.delete_person_from_event({"person_id":person_id, "event_id":event_id})
            QMessageBox.about(self, "Remove Person From Event", message)