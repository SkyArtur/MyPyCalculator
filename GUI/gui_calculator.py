from GUI.objects import *


class MyPyCalculator(CalcWidget):
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
        grid = [["7", "8", "9", "C", "Del"], ["4", "5", "6", "+", "/"], ["1", "2", "3", "-", "*"]]
        for pos in range(5):
            self.keyboard.grid.addWidget(CalcButton(self.keyboard, f'{grid[0][pos]}'), 1, pos, 1, 1)
            self.keyboard.grid.addWidget(CalcButton(self.keyboard, f'{grid[1][pos]}'), 2, pos, 1, 1)
            self.keyboard.grid.addWidget(CalcButton(self.keyboard, f'{grid[2][pos]}'), 3, pos, 1, 1)
        self.keyboard.grid.addWidget(CalcButton(self.keyboard, '.'), 4, 0, 1, 1)
        self.keyboard.grid.addWidget(CalcButton(self.keyboard, '0'), 4, 1, 1, 1)
        self.keyboard.grid.addWidget(CalcButton(self.keyboard, '='), 4, 2, 1, 3)
