from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QLabel, QMessageBox


class Input_Data_Widget(QWidget):
    def __init__(self, database_manipulator_add, title, textbox_properties, button_properties):
        super().__init__()
        self._db_manip = database_manipulator_add