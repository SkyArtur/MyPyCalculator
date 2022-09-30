from GUI.gui_calculator import MyPyCalculator
from GUI.objects import CalcApplication


def app_run() -> None:
    """
    The function runs the Calculator application.

    :return: None
    """
    calc_app = CalcApplication()
    calc_win = MyPyCalculator()
    calc_win.show()
    calc_app.exit_app()
