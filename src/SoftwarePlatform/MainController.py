"""This module handles the creation and initialisation of the main window.

The main window is created, with initialisation of the controller of each tab taking place.

    Typical usage example:

    python MainController.py
"""

import sys

from PyQt5 import QtWidgets
from ui_py.Main import Ui_MainWindow
from MainUploadTabController import MainUploadTabController
from MainResultsTabController import MainResultsTabController


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Initialises the main window of the user interface.

    Initialises the main window of the user interface and initialises the controller of each tab.
    
    """

    def __init__(self, *args, obj=None, **kwargs):
        """Initialises the main window of the user interface.

        Calls the init of the Ui_MainWindow class to initialise the necessary user interface components. Then initUiComponents is called to initialise the controller of each tab.

        Args:
            self: An instance of this class.
            *args: Arguments passed to the constructor.
            obj: An object passed to the constructor.
            **kwargs: Keyword arguments passed to the constructor.
        """
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.initUiComponents()

    def initUiComponents(self):
        """Initialises the controller of each tab.

        Creates and instance of each controller and initialises their ui components.

        Args:
            self: An instance of this class.
        """

        self.uploadController = MainUploadTabController(self)
        self.uploadController.initUiComponents()

        self.resultsController = MainResultsTabController(self)
        self.resultsController.initUiComponents()

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

if __name__ == '__main__':
    window.show()
    app.exec()
