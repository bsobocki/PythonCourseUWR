from PyQt5.QtWidgets import QPushButton

class Button(QPushButton):
    def __init__(self, x, y, text, tooltip, on_click, parent, width=120, height=30):
        super().__init__(text, parent)
        self.setToolTip( tooltip )
        self.move(x, y)
        self.resize( width, height )
        self.clicked.connect( on_click )