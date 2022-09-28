from GUI.gui_calculator import Caculadora
from GUI.objects import CalcApplication


def app_run() -> None:
    """
    The function runs the Calculator application.

    :return: None
    """
    app = CalcApplication()
    w = Caculadora()
    w.show()
    app.exit_app()
