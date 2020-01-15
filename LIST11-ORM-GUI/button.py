from PyQt5.QtWidgets import QPushButton

class Button(QPushButton):
    width = 120
    height = 30

    def __init__(self, x, y, text, tooltip, on_click, parent):
        super().__init__(text, parent)
        self.setToolTip( tooltip )
        self.move(x, y)
        self.resize( self.width, self.height )
        self.clicked.connect( on_click )