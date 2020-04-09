from PyQt5 import QtWidgets

from analysis import utils as analysis
from mainwindow import Ui_MainWindow


class MainController(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Initialize the MainController
        """
        super(MainController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_make_analysis.clicked.connect(analysis.pre_process_all_files)  # btn to tokenize all files


def run():
    """
    Runs the main window
    """
    app = QtWidgets.QApplication([])
    application = MainController()
    application.show()
    app.exec()
