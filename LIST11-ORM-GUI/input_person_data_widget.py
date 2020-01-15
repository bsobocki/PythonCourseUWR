from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QLabel, QMessageBox


class Input_Person_Data_Widget(QWidget):

    def __init__(self, type, database_manipulator):
        super().__init__()

        if type == "person_data" : self._init_person_data_UI()
        elif type == "event_data"  : self._init_event_data_UI()   
        else: raise Exception("Incorrect type of Input Widget!")

        self._db_manip = database_manipulator

        self.show()


    def _init_person_data_UI(self):
        self._label_title = self._create_label("Add person to the Calendar DataBase!", 10, x=50)

        y = 35
        self._label_name =  self._create_label("name", y)
        self._textbox_name = self._create_textbox(y)

        y += 30
        self._label_email = self._create_label("email", y)
        self._textbox_email = self._create_textbox(y)
    
        y+=30
        x = 216
        self._button_save = QPushButton("Add", self)
        self._button_save.setToolTip('Add to the DataBase!')
        self._button_save.move(x, y)
        self._button_save.clicked.connect(self._add_to_database)

        window_height = self._button_save.y() + self._button_save.height()+15
        self.setWindowTitle("Add Person To The DataBase")
        self.setGeometry(300, 300, 320, window_height)


    def get_data(self):
        return self._data


    def _add_to_database(self):
        result = self._db_manip.add_person({
            "name": self._textbox_name.text(),
            "email": self._textbox_email.text()
        })
        QMessageBox.about(self, "Adding Person To The Database", str(result))


    def _create_textbox(self, y, x=50, width=250, height=20):
        label = QLineEdit(self)
        label.move(x, y)
        label.resize(width,height)
        return label


    def _create_label(self, name, y, x=10):
        label = QLabel(name, self)
        label.move(x, y)
