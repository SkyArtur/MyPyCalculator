from GUI.objects import *


class CalcKeyboard(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.display = parent.display
        self.grid = QGridLayout(self)
        self.__config()

    def __config(self) -> None:
        """
        Grid settings.

        :return: None
        """
        self.setGeometry(QRect(10, 100, 321, 261))
        self.grid.setSpacing(2)
        self.grid.setContentsMargins(0, 0, 0, 0)
