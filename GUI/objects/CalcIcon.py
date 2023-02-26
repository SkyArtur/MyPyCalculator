from GUI.objects import *


class CalcIcon(QIcon):  # simple inheritance of the QIcon class
    def __init__(self):
        super().__init__()
        icon_path = os.path.join(
            Path(__file__).parent / 'icon', 'calc.ico'
        )
        self.addFile(icon_path, QSize())

    @property
    def icon(self) -> QIcon:
        """
        Returns the icon assigned to the class.

        :return: QIcon
        """
        return self

