from GUI.objects import *


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
