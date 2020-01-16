from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QLabel, QMessageBox

from button import Button


class Input_Data_Widget(QWidget):
    """
    params:
        @database_manipulator_add : DataBase_Manipulator_Add - the object that adding objects to the database
        @title : string - the window title
        @header_properties : dictionary with values:
            content : string - content of the label (the window header)
            x : int - x corrdinate
            y : int - y coordinate
        @button_properties : dictionary with values: 
            on_click : function - function that is called after pressing button
            content : string - text that is written on the button 
            tooltip : strin - tooltip of the button
        @inputs_properties : dictionary with values: 
            num : int - number of textboxes and labels that describes them,
            labels_contents : list of strings - contents of the given textboxes
    """
    def __init__(self, database_manipulator_add, title, header_properties, button_properties, inputs_properties):
        super().__init__()
        self._input_index = 0
        self._input_x = 10
        self._input_y = 5
        self._input_width = 250
        self._input_height = 20
        self._db_manip = database_manipulator_add
        self._title = title
        self._inputs_properties = inputs_properties
        self._header_properties = header_properties
        self._button_properties = button_properties
        self._labels = []
        self._textboxes = []

        self._init_UI()

        window_x, window_y = 300, 300
        window_height = self._button.y() + self._button.height() + 15
        window_width = self._textboxes[0].x() + self._textboxes[0].width() + 10
        self.setWindowTitle(self._title)
        self.setGeometry(window_x, window_y, window_width, window_height)


    def _init_UI(self):
        self._create_header()

        for i in range(0, self._inputs_properties["num"]): 
            self._add_next_input()

        self._add_button()


    def _create_header(self):
        self._header = QLabel(self._header_properties["content"], self)
        self._header.move(self._header_properties["x"], self._header_properties["y"])


    def _add_next_input(self):
        self._input_y += 30

        text = self._inputs_properties["labels_contents"][self._input_index]
        label = QLabel(text, self)
        label.move(self._input_x, self._input_y)
        self._labels.append(label)

        textbox = QLineEdit(self)
        textbox.move(self._input_x + label.width(), self._input_y)
        textbox.resize(self._input_width, self._input_height)
        self._textboxes.append(textbox)

        self._input_index += 1



    def _add_button(self):
        width = 120
        height = 30
        x = self._textboxes[0].x() + self._textboxes[0].width() - width
        self._input_y += 30

        self._button = Button(
            x=x, 
            y=self._input_y, 
            text=self._button_properties["content"],
            tooltip=self._button_properties["tooltip"],
            on_click=self._button_properties["on_click"],
            parent=self
        )