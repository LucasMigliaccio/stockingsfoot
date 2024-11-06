from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableView
from PySide6.QtCore import QAbstractTableModel, Qt
import pandas as pd


class PandasModel(QAbstractTableModel):
    def __init__(self, data_frame):
        super().__init__()
        self._data = data_frame

    def rowCount(self, index=None):
        return self._data.shape[0]

    def columnCount(self, index=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._data.columns[section]
            elif orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None