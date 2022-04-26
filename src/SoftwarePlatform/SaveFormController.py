"""This module handles the control of the save result dialog window.

Once the user has received a result from the upload and timing process, they can click the save button which initalises this module. This module configures the user interface of the save result dialog window, and allows the user to save the result to a file, as long as the data being saved matches the format of the log file being saved to.

    Typical usage example:

    saveDialog = SaveFormController()
	saveDialog.specifyResult(self.timerLabel.text().split(':')[1].lstrip())
	saveDialog.exec_()
"""

from ui_py.SaveForm import Ui_Dialog
from enum import Enum
from PyQt5 import QtGui, QtCore, QtWidgets

class SaveError(Enum):
	"""An enumeration of the possible errors that can occur when saving to a log file.

    The enumeration contains the possible errors that can occur when saving to a log file.

    Attributes:
        LINE_LENGTH_ERROR: A line in the log file does not contain the same number of parameters as the number of parameters being saved.
        PARAM_ERROR: A line in the log file does not contain one of the parameters being saved.
        RESULT_ERROR: 'RESULT' was not the final parameter in a line of the log file.
    """

	LINE_LENGTH_ERROR = 1
	PARAM_ERROR = 2
	RESULT_ERROR = 3

class SaveFormController(QtWidgets.QDialog, Ui_Dialog):
	"""Handles the saving of a result to a log file.

	This function handles the saving of a result to a log file. It allows the user to dynamically add parameters and their values to be saved alongside the result. Checks are carried out to ensure that the data being saved is in the correct format in comparison to the format of the output file. If so, the data is appended to the end of the log file.

	Attributes:
		_result: The result of the timer to be saved to the log file.
		_saved: A boolean indicating whether the result has been saved to the log file.
	"""

	_result = 0
	_saved = False

	def __init__(self, *args, obj=None, **kwargs):
		"""Initialises an instance of this class.

		This function initialises an instance of this class and calls the user interface components to be initialised.

		Args:
            self: An instance of this class.
            *args: Arguments passed to the constructor.
            obj: An object passed to the constructor.
            **kwargs: Keyword arguments passed to the constructor.
		"""
		
		super(SaveFormController, self).__init__(*args, **kwargs)
		self.setupUi(self)
		self.initUiComponents()


	def initUiComponents(self):
		"""Initialises the user interface components.
		
		This function initialises the user interface components by displaying and add record button, and setting the on click functions of the browse and save buttons.

		Args:
			self: An instance of this class.
		"""

		self.recordVerticalLayout.setAlignment(QtCore.Qt.AlignTop)
		self.showAddRecordButton()
		self.btnBrowse.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DirIcon))
		self.btnBrowse.clicked.connect(self.browseFiles)
		self.buttonBox.accepted.connect(self.saveResult)


	def showAddRecordButton(self):
		"""Adds the add record button to the bottom of the list of records.

		This function adds the add record button to the bottom of the list of paramaters, to allow the user to add another record to the list. 

		Args:
			self: An instance of this class.
		"""

		hbox = QtWidgets.QHBoxLayout()

		addButton = QtWidgets.QToolButton()
		addButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		addButton.setIcon(QtGui.QIcon("./bin/sign-add-icon.png"))
		addButton.setText('  Add Record')
		addButton.clicked.connect(self.addRecord)
		addButton.setAutoRaise(True)

		hbox.addWidget(addButton)
		self.recordVerticalLayout.addRow(hbox)


	def addRecord(self):
		"""Dynamically add a record to save to the file.

		This function dynamically adds a record to be saved to the file. Each record includes a name for the parameter and its value to be saved togetherer as a pair to the log file. Each record is added to the bottom of the list of records along with a remove button to allow the user to dynamically remove records.

		Args:
			self: An instance of this class.
		"""

		hbox = QtWidgets.QHBoxLayout()

		paramLineEdit = QtWidgets.QLineEdit()
		paramLineEdit.setPlaceholderText('Parameter')
		paramLineEdit.textChanged.connect(lambda: paramLineEdit.setStyleSheet('color : black;'))
		hbox.addWidget(paramLineEdit)

		valueLineEdit = QtWidgets.QLineEdit()
		valueLineEdit.setPlaceholderText('Value')
		valueLineEdit.textChanged.connect(lambda: valueLineEdit.setStyleSheet('color : black;'))
		valueLineEdit.setValidator(QtGui.QDoubleValidator())
		hbox.addWidget(valueLineEdit)

		deleteButton = QtWidgets.QToolButton()
		deleteButton.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_TrashIcon))
		hbox.addWidget(deleteButton)
		deleteButton.clicked.connect(self.removeRecord)

		self.recordVerticalLayout.addRow(hbox)
		self.updateAddRecordButton()


	def removeRecord(self):
		"""Removes a parameter and value record from the list of records.
		
		This function removes the selected parameter and value record from the list of parameters and values.

		Args:
			self: An instance of this class.
		"""

		for i in range(self.recordVerticalLayout.rowCount()):

			item = self.recordVerticalLayout.itemAt(i, QtWidgets.QFormLayout.FieldRole).itemAt(2)


			if not item == None and self.sender() == item.widget():

				self.recordVerticalLayout.removeRow(i)
				self.updateAddRecordButton()
				break


	def removeAddRecordButton(self):
		"""Removes the add record button from the bottom of the list of records.
		
		This function removes the add record button from the bottom of the list of ESP devices, to allow it to be added again later.

		Args:
			self: An instance of this class.
		"""

		for i in range(self.recordVerticalLayout.rowCount()):

			item = self.recordVerticalLayout.itemAt(i, QtWidgets.QFormLayout.FieldRole).itemAt(2)

			if item == None:

				self.recordVerticalLayout.removeRow(i)
				break


	def updateAddRecordButton(self):
		"""Updates the add record button such that it is always placed below all records.

		This function firstly removes the add record button from the list of records, and then adds it again to the bottom of the list to ensure it always remains below all records.

		Args:
			self: An instance of this class.
		"""

		self.removeAddRecordButton()
		self.showAddRecordButton()


	def specifyResult(self, time):
		"""Sets the result text box to display the result of the timing.

		This function sets the result text box to display the result of the timing.

		Args:
			self: An instance of this class.
			time: The result of the time taken.
		"""

		global _result
		_result = time
		self.labelResult.setText(f'Result: {_result}')


	def browseFiles(self):
		"""Displays a dialog window that allows the user to select a text file to append their result to.

        Displays a dialog window that allows the user to select a text file to append their result to. The selected file is later checked to ensure it follows the same format as the data being saved by the user.

        Args:
            self: An instance of this class.
		"""

		tempFile, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Save to Log File', QtCore.QDir.rootPath(), '*.txt')

		if tempFile != '' and tempFile != self.filenameLineEdit.text():
			self.filenameLineEdit.setStyleSheet('color : black;')
			self.filenameLineEdit.setText(tempFile)


	def saveResult(self):
		"""Saves the result to the file.

		If the format of the file to be saved to and the format of the data being saved are the same, the result is saved to the file.

		Args:
			self: An instance of this class.
		"""

		self.params = []
		self.values = []

		self.labelError.setText('')

		if self.checkIfPathIsEmpty():
			return

		if self.checkIfParamIsEmpty():
			return

		self.saveToFile()


	def checkIfPathIsEmpty(self):
		"""Checks if the path of the file to save to is empty.

		This function checks if the path of the file to save to is empty. If it is, an error message is displayed to the user.

		Args:
			self: An instance of this class.

		Returns:
			True if the path is empty, False otherwise.
		"""

		if not self.filenameLineEdit.text():
			self.filenameLineEdit.setStyleSheet('color : red;')
			self.filenameLineEdit.setText('ERROR: Path must not be empty.')
			return True
		return False


	def checkIfParamIsEmpty(self):
		"""Checks if the parameter name or its value is empty.
		
		This function checks if the parameter name or its value is empty. If it is, an error message is displayed to the user.

		Args:
			self: An instance of this class.
		
		Returns:
			True if the parameter name or its value is empty, False otherwise.
		"""

		for i in range(self.recordVerticalLayout.rowCount() - 1):
			paramBox = self.recordVerticalLayout.itemAt(i, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget()
			valueBox = self.recordVerticalLayout.itemAt(i, QtWidgets.QFormLayout.FieldRole).itemAt(1).widget()

			if not paramBox.text() or paramBox.text() == 'Field must not be empty.':

				paramBox.setText('Field must not be empty.')
				paramBox.setStyleSheet('color : red;')
				return True

			if not valueBox.text() or valueBox.text() == 'Field must not be empty.':

				valueBox.setText('Field must not be empty.')
				valueBox.setStyleSheet('color : red;')
				return True

			self.params.append(paramBox.text())
			self.values.append(valueBox.text())

		return False


	def saveToFile(self):
		"""Saves the data to the file if there are no errors.

		This function saves the parameters, their values and the result to the file if there are no errors.

		Args:
			self: An instance of this class.
		"""

		file = open(self.filenameLineEdit.text(), 'a+')
		file.seek(0)
		lines = [line.rstrip() for line in file]

		outputString, error = self.checkIfSaveToFileError(self.params, self.values, lines)

		if not error:
			global _saved
			outputString += f'RESULT:{_result}'
			file.write(f'{outputString}\n')
			file.close()
			_saved = True
			self.close()
		else:
			file.close()


	def checkIfSaveToFileError(self, params, values, lines):
		"""Checks if there are any errors with the file.

		This function checks if there are any inconsistencies with the data being appended to the file and the format of the file currently. If there are any, handleSaveToFileError is called.

		Args:
			self: An instance of this class.
			params: The parameters to be saved.
			values: The values of the parameters to be saved.
			lines: The lines of the file.

		Returns:
			The output string to be saved to the file along with True if there were errors and False otherwise.
		"""

		outputString = ''

		for i in range(len(lines)):
			fileParams = lines[i].split(',')

			if not len(fileParams) - 1 == len(params):
				self.handleSaveToFileError(SaveError.LINE_LENGTH_ERROR, unmatchedLineIndex=i)
				return [outputString, True] 

			for j in range(len(params)):
				if not params[j].upper() == fileParams[j].split(':')[0]:
					self.handleSaveToFileError(SaveError.PARAM_ERROR, j, i)
					return [outputString, True]

			resultStrings = fileParams[len(fileParams) - 1].split(':')
			if not resultStrings[0] == 'RESULT':
				self.handleSaveToFileError(SaveError.RESULT_ERROR, unmatchedLineIndex=i)
				return [outputString, True]

		for n in range(len(params)):
			outputString += f'{params[n].upper()}:{values[n]},'

		return [outputString, False]


	def handleSaveToFileError(self, error, unmatchedParamIndex=0, unmatchedLineIndex=0):
		"""Ensures that the correct error message is displayed to the user when a save to file error is detected.

        This function uses the SaveError enum class to determine what the error is, and displays the correct error message to the user.

        Args:
            self: An instance of this class.
            error: The error enum that was detected.
            unmatchedParamIndex: The index of the parameter that was unmatched.
			unmatchedLineIndex: The index of the line that was unmatched.
        """

		if error == SaveError.LINE_LENGTH_ERROR:
			self.labelError.setText(f'Number of parameters do not match length of line {unmatchedLineIndex + 1}.')
			self.labelError.setStyleSheet('color : red;')
		elif error == SaveError.PARAM_ERROR:
			self.recordVerticalLayout.itemAt(unmatchedParamIndex, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().setText(f'Param not in log file, line {unmatchedLineIndex + 1}.')
			self.recordVerticalLayout.itemAt(unmatchedParamIndex, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().setStyleSheet('color : red;')
		elif error == SaveError.RESULT_ERROR:
			self.labelError.setText(f'Result not found in line {unmatchedLineIndex + 1}.')
			self.labelError.setStyleSheet('color : red;')


	def getSaved(self):
		"""Returns if the result has been saved or not.

		This function returns if the result has been saved or not.

		Args:
			self: An instance of this class.

		Returns:
			True if the result has been saved, False otherwise.
		"""

		return _saved