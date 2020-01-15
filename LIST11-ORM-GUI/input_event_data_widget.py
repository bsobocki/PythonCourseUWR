from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QLabel, QMessageBox


class Input_Event_Data_Widget(Input_Data_Widget):
    def __init__(self, database_manipulator_add):
        super().__init__(database_manipulator_add)
        
        self._init_UI() 
        self.show()