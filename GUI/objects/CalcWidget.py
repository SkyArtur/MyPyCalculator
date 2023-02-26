from GUI.objects import *


class CalcWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__config()

    def __config(self) -> None:
        """
        Objects settings.

        :return: None
        """
        self.setWindowIcon(CalcIcon().icon)
        self.setWindowTitle('Calculadora')
        self.setProperty('class', 'widget')
        self.setFixedSize(345, 375)
        self.setStyleSheet(stylesheet_widget)
