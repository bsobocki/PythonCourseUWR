from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QLabel, QMessageBox

from input_data_widget import Input_Data_Widget

class Input_Event_Data_Widget(Input_Data_Widget):
    def __init__(self, database_manipulator_add):
        super().__init__(
            database_manipulator_add, 
            title="Add Event", 
            header_properties={
                "content" : "Complete the fields and click 'Add Event' to add.",
                "x" : 10,
                "y" : 10
            }, 
            button_properties={
                "on_click" : self._add_to_database,
                "content" : "Add Event",
                "tooltip" : "You can add a new event to the DataBase!"
            }, 
            inputs_properties={
                "num" : 3,
                "labels_contents" : ["title", "starts at", "ends at"]
            })
        self.show()


    def get_data(self):
        return self._data


    def _add_to_database(self):
        result = self._db_manip.add_event({
            "title": self._textboxes[0].text(),
            "start_time": self._textboxes[1].text(),
            "end_time": self._textboxes[2].text()
        })
        QMessageBox.about(self, "Adding Event To The Database", str(result))