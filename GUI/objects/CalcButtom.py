from GUI.objects import *


class CalcButton(QPushButton):
    def __init__(self, parent, text: str):
        super().__init__(parent, text=text)
        self.input = parent.display
        self.__config()

    def __config(self) -> None:
        """
        Buttons settings. Checks the content of the button's text to
        select the style sheet to be applied.

        :return: None
        """
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        font = QFont(u"Bahnschrift", 15)
        self.setFocusPolicy(Qt.NoFocus)
        self.setProperty('class', 'btn')
        self.setSizePolicy(size_policy)
        self.setFont(font)
        if self.text() in 'Del':
            self.setStyleSheet(stylesheet_btn_del)
        elif self.text().isnumeric():
            self.setStyleSheet(stylesheet_btn_numbers)
        else:
            self.setStyleSheet(stylesheet_btn_operators)

    def mousePressEvent(self, event: QMouseEvent) -> QLineEdit.setText:
        """
        QPushButton class override function.

        :param event: click mouse.
        :return: str | None
        """
        super(CalcButton, self).mousePressEvent(event)
        if self.text() in "C":  # Minus the last character of the string
            return self.input.setText(self.input.text()[:-1])
        elif self.text() in "Del":  # Clear display's text and placeholder text
            self.input.clear()
            return self.input.setPlaceholderText('')
        elif self.text() in "/*-+":  # Do not leave writing on the display if there is nothing written on it.
            if not self.input.result:
                if self.text() not in '-+':  # except if the buttons are + and -
                    return
            else:
                if self.input.result not in '/*':
                    self.input.setText(self.input.result)
        elif self.text() in ".":  # Checks previous entry by clicking the "dot" key and inserts zero where relevant.
            for check in ['', '+', '-', '/', '*']:
                if self.input.text() == check or self.input.text()[-1] == check:
                    return self.input.setText(self.input.text() + "0" + self.text())
        elif self.text() in "=":  # Tries to calculate display content using the built-in eval function
            try:
                self.input.setPlaceholderText(self.input.result)
                return self.input.clear()
            except TypeError:
                return
        return self.input.setText(self.input.text() + self.text())
