from PySide6.QtWidgets import QApplication, QGridLayout, QLineEdit, QPushButton, QSizePolicy, QWidget
from PySide6.QtGui import QFont, QFontDatabase, QMouseEvent, QIcon
from PySide6.QtCore import QRect, QSize, Qt
from GUI.objects.stylesheets import *
from pathlib import Path
import sys
import os


# I chose to create my objects by inheritance to have a cleaner code.

class CalcApplication(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

    @staticmethod  # This way I can call method without instantiating the class.
    def exit_app() -> sys.exit:
        """
        Closes the program.

        :return: sys.exit
        """
        return sys.exit(CalcApplication.exec())


class CalcIcon(QIcon):  # simple inheritance of the QIcon class
    def __init__(self, dirs: str, files: str):
        super().__init__()
        ICON_PATH = os.path.join(Path(__file__).parent / dirs, files)
        self.addFile(ICON_PATH, QSize(), self.Normal, self.Off)

    @property
    def icon(self) -> QIcon:
        """
        Returns the icon assigned to the class.

        :return: QIcon
        """
        return self


class CalcDisplayFont(QFont):
    def __init__(self, dirs: str, files: str):
        super().__init__()
        FONT_PATH = os.path.join(Path(__file__).parent / dirs, files)
        QFontDatabase.addApplicationFont(FONT_PATH)
        self.setFamily(u"Digital-7")
        self.setPointSize(55)

    @property
    def font(self) -> QFont:
        """
        Returns the chosen Font for the display.

        :return: QFont
        """
        return self


class CalcWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__config()

    def __config(self) -> None:
        """
        Objects settings.

        :return: None
        """
        self.setWindowIcon(CalcIcon('icon', 'calc.ico').icon)
        self.setWindowTitle('Calculadora')
        self.setProperty('class', 'widget')
        self.setFixedSize(345, 375)
        self.setStyleSheet(stylesheet_widget)


class CalcKeyboard(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.display = parent.display
        self.grid = QGridLayout(self)
        self.config()

    def config(self) -> None:
        """
        Grid settings.

        :return: None
        """
        self.setGeometry(QRect(10, 100, 321, 261))
        self.grid.setSpacing(2)
        self.grid.setContentsMargins(0, 0, 0, 0)


class CalcDisplay(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.__config()

    def __config(self) -> None:
        """
        Display settings.

        :return: None
        """
        self.setFont(CalcDisplayFont('fonts', "Digital7-1e1Z.ttf").font)
        self.setGeometry(QRect(10, 10, 320, 80))
        self.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.setEnabled(False)
        self.setProperty('class', 'display')
        self.setStyleSheet(stylesheet_display)


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
        elif self.text() in "/*":  # Do not leave writing on the display if there is nothing written on it.
            if self.input.text() == "" or self.input.text() is None:
                return
        elif self.text() in "=":  # Tries to calculate display content using the built-in eval function
            try:
                self.input.setPlaceholderText(str(eval(self.input.text())))
                return self.input.clear()
            except Exception as error:
                return error
        return self.input.setText(self.input.text() + self.text())
