from GUI.objects import *


class CalcDisplayFont(QFont):
    def __init__(self):
        super().__init__()
        font_path = os.path.join(
            Path(__file__).parent / 'fonts', "Digital7-1e1Z.ttf"
        )
        QFontDatabase.addApplicationFont(font_path)
        self.setFamily(u"Digital-7")
        self.setPointSize(45)

    @property
    def font(self) -> QFont:
        """
        Returns the chosen Font for the display.

        :return: QFont
        """
        return self
