from GUI.objects import *


class Caculadora(CalcWidget):
    """
    Calculator main window.

    """
    def __init__(self):
        super().__init__()
        self.display = CalcDisplay(self)
        self.keyboard = CalcKeyboard(self)
        self.config_keyboard()

    def config_keyboard(self) -> None:
        """
        Configures calculator keyboard buttons.

        :return: None
        """
        lines = [["7", "8", "9", "C", "Del"], ["4", "5", "6", "+", "/"], ["1", "2", "3", "-", "*"]]
        for grid in range(5):
            self.keyboard.grid.addWidget(CalcButton(self.keyboard, f'{lines[0][grid]}'), 1, grid, 1, 1)
            self.keyboard.grid.addWidget(CalcButton(self.keyboard, f'{lines[1][grid]}'), 2, grid, 1, 1)
            self.keyboard.grid.addWidget(CalcButton(self.keyboard, f'{lines[2][grid]}'), 3, grid, 1, 1)
        self.keyboard.grid.addWidget(CalcButton(self.keyboard, '.'), 4, 0, 1, 1)
        self.keyboard.grid.addWidget(CalcButton(self.keyboard, '0'), 4, 1, 1, 1)
        self.keyboard.grid.addWidget(CalcButton(self.keyboard, '='), 4, 2, 1, 3)
