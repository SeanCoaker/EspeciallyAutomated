"""This module handles the control of the results tab of the main window.

Once the main window is created, this module is called to initialise the controller of the results tab. The module handles the loading of the user's log files and converts them into matplotlib subplots. When the user attempts to load a log file, this module ensures that the log file is compatible for the rendering of the log file.

    Typical usage example:

    resultsController = MainResultsTabController(self)
    resultsController.initUiComponents()
"""

import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir
from enum import Enum
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class LoadError(Enum):
    """An enumeration of the possible errors that can occur when loading a log file.

    The enumeration contains the possible errors that can occur when loading a log file.

    Attributes:
        LAST_PARAM_ERROR: Result not found in the last parameter of a line in the log file.
        LINE_LENGTH_ERROR: A line in the log file does not contain the same number of parameters as the first line.
        PARAM_MATCH_ERROR: A line in the log file does not contain the same parameters as the first line.
        PARAM_FLOAT_ERROR: A parameter in the log file is not a float.
    """

    LAST_PARAM_ERROR = 1
    LINE_LENGTH_ERROR = 2
    PARAM_MATCH_ERROR = 3
    PARAM_FLOAT_ERROR = 4


class MainResultsTabController():
    """Handles the initialisation of the user interface components included within the results tab, as well as the loading of the user's log files into matplotlib subplots.

    This class initialises user interface components that are included within the main window's results tab, and includes functions that allow log files to be loaded into matplotlib subplots. Further functions are included that ensure that the log file is compatible with the plots that the system aims to render.

    Attributes:
        _ui: 
            An instance of MainController to access its user interface components.
        _paramValueMap: 
            A dictionary that contains the parameters and their corresponding values.
        _checkboxes: 
            A list of checkboxes that are included within the results tab. These checkboxes represent the parameters that the user wishes to display in the subplots of.
        _selectedParams:
            A dictionary of the parameters and whether they should be displayed in the subplots or not.
        _fileLoadComplete:
            A boolean that indicates whether loading of a log file has been completed.
    """

    _ui = None
    _paramValueMap = {}
    _checkboxes = []
    _selectedParams = {}
    _fileLoadComplete = False

    def __init__(self, parent):
        """Initialises this class.

        Initialises this class and assigns the _ui attribute to be the parent object (MainController object).

        Args:
            self: An instance of this class.
            parent: The parent object (MainController object).
        """

        self._ui = parent

    def initUiComponents(self):
        """Initialises the user interface components of the results tab.

        Sets the browse button to include an image of a folder, and assigns a function to be run when the browse button is clicked.

        Args:
            self: An instance of this class.
        """

        self._ui.btnResultBrowse.setIcon(self._ui.style().standardIcon(QtWidgets.QStyle.SP_DirIcon))
        self._ui.btnResultBrowse.clicked.connect(self.browseLoadFiles)

    def browseLoadFiles(self):
        """Displays a dialog window that allows the user to select a text file to be loaded.

        Displays a dialog window that allows the user to select a text file to be loaded. The path of the selected file is then copied into the file text box, and an attempt is made to render matplotlib subplots from the selected file.

        Args:
            self: An instance of this class.
        """

        tempFile, _ = QtWidgets.QFileDialog.getOpenFileName(self._ui, 'Load Log File', QDir.rootPath(), '*.txt')

        if tempFile != '':
            self._ui.resultFileLineEdit.setStyleSheet('color : black;')
            self._ui.resultFileLineEdit.setText(tempFile)
            file = open(self._ui.resultFileLineEdit.text(), 'r')
            file.seek(0)
            self.loadResults(file)
            file.close()

    def loadResults(self, file):
        """Begins the load process of the log file.

        Should the log file not return any errors, this function attemps to clear the user interface of the results and render to the new subplots.

        Args:
            self: An instance of this class.
            file: The log file to be loaded.
        """

        if os.stat(os.path.realpath(file.name)).st_size == 0:
            self._ui.loadErrorLabel.show()
            self._ui.loadErrorLabel.setStyleSheet('color : red;')
            self._ui.loadErrorLabel.setText('File is empty.')
            return

        self._ui.loadErrorLabel.hide()

        self._fileLoadComplete = False

        self.clearParams()
        if not self.checkIfLoadFileError(file):
            self.setCheckboxes()
            self.setCombobox()
            self.displayPlots()

            self._fileLoadComplete = True

    def clearParams(self):
        """Clears the parameters and their corresponding values.

        This function clears the parameters and their corresponding values, as well as clearing the list of checkboxes that allow the user to selected which parameters to display in the subplots.

        Args:
            self: An instance of this class.
        """

        self._paramValueMap.clear()

        while self._ui.paramsGrid.count():
            child = self._ui.paramsGrid.takeAt(0)

            if child.widget():
                child.widget().deleteLater()

    def checkIfLoadFileError(self, file):
        """ Checks if the log file has any errors.

        This function checks the log file to ensure that each line is of the same format and that the format is compatible with the loading of the log file into matplotlib subplots.

        Args:
            self: An instance of this class.
            file: The log file to be checked.

        Returns:
            True if an error was detected, False otherwise.
        """

        lines = [line.rstrip() for line in file]
        firstLineParamsAndValues = lines[0].split(',')

        if not firstLineParamsAndValues[len(firstLineParamsAndValues) - 1].split(':')[0] == 'RESULT':
            self.handleLoadError(LoadError.LAST_PARAM_ERROR, 1)
            return True

        for i in range (len(lines)):

            lineParamsAndValues = lines[i].split(',')

            if not lineParamsAndValues[len(lineParamsAndValues) - 1].split(':')[0] == 'RESULT':
                self.handleLoadError(LoadError.LAST_PARAM_ERROR, i + 1)
                return True

            if not len(firstLineParamsAndValues) == len(lineParamsAndValues):
                self.handleLoadError(LoadError.LINE_LENGTH_ERROR, i + 1)
                return True

            for j in range(len(lineParamsAndValues)):
                paramAndValue = lineParamsAndValues[j].split(':')

                if not paramAndValue[0] == firstLineParamsAndValues[j].split(':')[0]:
                    self.handleLoadError(LoadError.PARAM_MATCH_ERROR, i + 1)
                    return True

                if not self.isFloat(paramAndValue[1]):
                    self.handleLoadError(LoadError.PARAM_FLOAT_ERROR, i + 1)
                    return True

                if paramAndValue[0] not in self._paramValueMap:
                    self._paramValueMap[paramAndValue[0]] = []

                self._paramValueMap[paramAndValue[0]].append(paramAndValue[1])

        return False


    def handleLoadError(self, error, lineNum):
        """Ensures that the correct error message is displayed to the user when a file error is detected.

        This function uses the LoadError enum class to determine what the error is, and displays the correct error message to the user.

        Args:
            self: An instance of this class.
            error: The error enum that was detected.
            lineNum: The line number that the error occurred on.
        """

        self._ui.loadErrorLabel.show()
        self._ui.loadErrorLabel.setStyleSheet('color : red;')

        self.clearPlots()
        self.clearParams()

        if error == LoadError.LAST_PARAM_ERROR:
            self._ui.loadErrorLabel.setText(f'RESULT parameter should appear last on Line {lineNum}.')

        elif error == LoadError.LINE_LENGTH_ERROR:
            self._ui.loadErrorLabel.setText(f'Number of parameters in Line {lineNum} does not match Line 1.')

        elif error == LoadError.PARAM_MATCH_ERROR:
            self._ui.loadErrorLabel.setText(f'A parameter in Line {lineNum} does not match the parameters in Line 1.')

        elif error == LoadError.PARAM_FLOAT_ERROR:
            self._ui.loadErrorLabel.setText(f'Value of a parameter in Line {lineNum} is not a float.')

    def isFloat(self, string):
        """Checks if the string is a float.

        This function checks if the string being passed in is a float. This is utilised to ensure that values associated with parameters are floats.

        Args:
            self: An instance of this class.
            string: The string to be checked.

        Returns:
            True if the string is a float, False otherwise.
        """

        try:
            float(string)
            return True
        except ValueError:
            return False

    def clearPlots(self):
        """Clears the plots.
        
        This function clears all subplots from the user interface. This function is called when a new log file is being loaded.
        
        Args:
            self: An instance of this class.
        """

        while self._ui.gridLayout.count():
            child = self._ui.gridLayout.takeAt(0)

            while(child.count()):
                subchild = child.takeAt(0)
                if subchild.widget():
                    subchild.widget().deleteLater()

            if child.widget():
                child.widget().deleteLater()

        self._ui.gridLayout.update()

    def setCheckboxes(self):
        """Displays new checkboxes for the parameters depending on the parameters in the log file.

        This function displays new checkboxes for the parameters depending on the parameters in the log file. This is called when a new log file is being loaded. Checkboxes are displayed in a grid layout of 3 columns.

        Args:
            self: An instance of this class.
        """

        self._checkboxes = []

        r = 0
        c = 0

        for param in self._paramValueMap:

            if param == 'RESULT':
                continue

            self._selectedParams[param] = True

            checkbox = QtWidgets.QCheckBox(param, self._ui)
            checkbox.stateChanged.connect(self.toggleCheckbox)
            checkbox.setChecked(True)
            self._ui.paramsGrid.addWidget(checkbox, r, c)
            self._checkboxes.append(checkbox)

            if c == 2:
                c = 0
                r += 1
            else:
                c += 1

    def toggleCheckbox(self, checked):
        """Toggles the state of the clicked checkbox.

        This function toggles the state of the clicked checkbox. If a file has been loaded then the subplots are refreshed to only display the selected parameters. Parameters are selected by selecting the parameter checkboxes.

        Args:
            self: An instance of this class.
            checked: The checked state of the checkbox.
        """

        checkbox = self._ui.sender()
        self._selectedParams[checkbox.text()] = (checked == 2)
        
        if self._fileLoadComplete:
            self.displayPlots()

    def setCombobox(self):
        """Sets the list of items in the combo box.
        
        Appends a list of the file's parameters to the combo box, as well as options for all parameters or no parameters.

        Args:
            self: An instance of this class.
        """

        comboList = list(self._paramValueMap.keys())
        comboList.insert(0, 'ALL')
        comboList.append('NONE')
        comboList.remove('RESULT')
        self._ui.comboBox.clear()
        self._ui.comboBox.addItems(comboList)
        self._ui.comboBox.setCurrentIndex(0)
        self._ui.comboBox.currentTextChanged.connect(self.selectComboItem)

    def selectComboItem(self, text):
        """Sets the state of the checkboxes depending on what combo box item was selected.
        
        This function sets the state of the checkboxes depending on what combo box item was selected. If a single parameter was selected from the combo box, then only hat checkbox is selected, if the 'all' option is selected then all checkboxes are selected, and if the 'none' option is selected then all checkboxes are deselected.

        Args:
            self: An instance of this class.
            text: The text of the selected combo box item.
        """

        self.uncheckAllCheckboxes()

        if text == 'ALL':
            for param in self._selectedParams:
                self._selectedParams[param] = True
        elif not text == 'NONE':
            self._selectedParams[text] = True

        self.checkSelectedCheckboxes()

    def uncheckAllCheckboxes(self):
        """Unchecks all checkboxes.

        This function unchecks all checkboxes and sets all key value pairs of the _selectedParams dictionary to False.

        Args:
            self: An instance of this class.
        """

        for checkbox in self._checkboxes:
            checkbox.setChecked(False)
            self._selectedParams[checkbox.text()] = False


    def checkSelectedCheckboxes(self):
        """Checks all selected checkboxes.
        
        This function sets the value of all keys in the _selectedParams dictionary to True if their respective checkbox is selected.

        Args:
            self: An instance of this class.
        """

        for checkbox in self._checkboxes:
            if self._selectedParams[checkbox.text()] == True:

                checkbox.setChecked(True)

    def displayPlots(self):
        """Displays all selected subplots to be displayed.
        
        This function displays all selected subplots to be displayed. The imported results are converted to floats and then plotted against the values of each of the selected parameters. The grid layout of subplots are 2 columns wide.

        Args:
            self: An instance of this class.
        """

        r = 0
        c = 0

        self.clearPlots()

        y = [float(x) for x in self._paramValueMap['RESULT']]

        for param in self._paramValueMap:

            if param == 'RESULT':
                continue

            if self._selectedParams[param] == True:
                figure = Figure(figsize=(1,1), tight_layout=False)
                ax = figure.add_subplot(111)
                x = [float(x) for x in self._paramValueMap[param]]
                ax.scatter(x, y)
                ax.title.set_text(f'{param} to Result')
                ax.set_xlabel(param)
                ax.set_ylabel('RESULT')

                canvas = FigureCanvas(figure)
                canvas.setMinimumSize(400, 400)
                canvas.draw()

                toolbar = NavigationToolbar(canvas, self._ui)
                layout = QtWidgets.QVBoxLayout()
                layout.addWidget(toolbar)
                layout.addWidget(canvas)

                self._ui.gridLayout.addLayout(layout, r, c)

                if c == 1:
                    c = 0
                    r += 1
                else:
                    c += 1
