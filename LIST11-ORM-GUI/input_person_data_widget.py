from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QLabel, QMessageBox

from input_data_widget import Input_Data_Widget

class Input_Person_Data_Widget(Input_Data_Widget):
    def __init__(self, database_manipulator_add):
        super().__init__(
            database_manipulator_add, 
            title="Add Person", 
            header_properties={
                "content" : "Complete the fields and click 'Add Person' to add.",
                "x" : 10,
                "y" : 10
            }, 
            button_properties={
                "on_click" : self._add_to_database,
                "content" : "Add Person",
                "tooltip" : "You can add a new person to the DataBase!"
            }, 
            inputs_properties={
                "num" : 2,
                "labels_contents" : ["name", "email"]
            })
        self.show()


    def get_data(self):
        return self._data


    def _add_to_database(self):
        result = self._db_manip.add_person({
            "name": self._textboxes[0].text(),
            "email": self._textboxes[1].text()
        })
        QMessageBox.about(self, "Adding Person To The Database", str(result))