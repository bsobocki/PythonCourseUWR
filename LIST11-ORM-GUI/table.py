from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class Table(QTableWidget):
    def __init__(self, x, y, parent):
        super().__init__(parent)        
        self.resize(319, 200)
        self.move(x,y)

        
    def _add_items(self, items):
        self.setRowCount(len(items))

        for j in range(0, len(items)):
            for i in range(0, len(items[0])):
                self.setItem( j, i, QTableWidgetItem(str(items[j][i])) )


    def _remove_data(self):
        for i in range(0, self.rowCount()): self.removeRow(i)



    def update_data(self, column_names, items):
        self._remove_data()
        self.setColumnCount(len(column_names))
        self.setHorizontalHeaderLabels(column_names)
        self.setRowCount(len(items))
        self._add_items(items)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()