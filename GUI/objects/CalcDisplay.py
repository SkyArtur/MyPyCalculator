from GUI.objects import *


class CalcDisplay(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self._result = None
        self.__config()

    @property
    def result(self):
        try:
            self._result = round(eval(self.text()), 7)
        except SyntaxError:
            return False
        return str(self._result)

    def __config(self) -> None:
        """
        Display settings.

        :return: None
        """
        self.setFont(CalcDisplayFont().font)
        self.setGeometry(QRect(10, 10, 320, 80))
        self.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.setEnabled(False)
        self.setProperty('class', 'display')
        self.setStyleSheet(stylesheet_display)

