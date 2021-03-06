from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class Table(QTableWidget):
    def __init__(self, x, y, width, parent):
        super().__init__(parent)        
        self.resize(width, 200)
        self.move(x,y)

        
    def _add_items(self, items):
        self.setRowCount(len(items))

        for j in range(0, len(items)):
            for i in range(0, len(items[0])):
                self.setItem( j, i, QTableWidgetItem(str(items[j][i])) )


    def remove_selected(self):
        for item in self.selectedItems():
            self.removeRow(item.row())


    def get_ids_of_selected(self):
        id_vals = []
        for item in self.selectedItems():
            id_vals.append( int(self.item( item.row(), 0).text()) )
        return id_vals


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