"""This module handles control of the upload tab of the main window.

Once the main window is created, this module is called to initialise the controller of the upload tab. The module allows the user to enter details for the upload process and begin the upload.

	Typical usage example:

    uploadController = MainUploadTabController(self)
	uploadController.initUiComponents()
"""

import os

from PyQt5 import QtWidgets, QtGui, QtCore
from UploadDialogController import UploadDialogController

class MainUploadTabController():
	"""Handles the initialisation of the user interface components included within the upload tab, and allows the user to begin the sketch upload and timing process.

    This class initialises user interface components that are included within the main window's upload tab, and includes functions that allows the user to being the process of uploading and timing Arduino sketches. Further functions are included that ensure that compatible data is being entered as required information for the upload process.

    Attributes:
        _ui: 
            An instance of MainController to access its user interface components.
    """

	_ui = None

	def __init__(self, parent):
		"""Initialises this class.

        Initialises this class and assigns the _ui attribute to be the parent object (MainController object).

        Args:
            self: An instance of this class.
            parent: The parent object (MainController object).
        """

		global _ui
		_ui = parent

	def initUiComponents(self):
		"""Initialises the user interface components included within the upload tab.

		This function initialises the user interface components included within the main window's upload tab, configuring their appearance and functionality when the user clicks on them. Before completing, the function ensures that a record for an ESP device to be uploaded to is added to ensure that the user cannot attempt to upload to an empty list of devices.

		Args:
			self: An instance of this class.
		"""

		_ui.startButton.clicked.connect(self.startUploadDialog)
		_ui.btnSketch.setIcon(_ui.style().standardIcon(QtWidgets.QStyle.SP_DirIcon))
		_ui.btnSketch.clicked.connect(self.browseSketchFiles)
		_ui.otaPortLineEdit.setValidator(QtGui.QIntValidator())
		_ui.udpPortLineEdit.setValidator(QtGui.QIntValidator())
		_ui.deviceIpLineEdit.textChanged.connect(lambda: _ui.deviceIpLineEdit.setStyleSheet('color : black;'))
		_ui.udpPortLineEdit.textChanged.connect(lambda: _ui.udpPortLineEdit.setStyleSheet('color : black;'))
		_ui.otaPortLineEdit.textChanged.connect(lambda: _ui.otaPortLineEdit.setStyleSheet('color : black;'))

		self.addEsp()


	def addEsp(self):
		"""Dynamically add a record of an ESP device to be uploaded to.

		This function dynamically adds a record of an ESP device to be uploaded to the list of ESP devices. Each record includes a name for the ESP and its IP address. Each record except the first includes a delete button to allow the record to be removed.

		Args:
			self: An instance of this class.
		"""

		hbox = QtWidgets.QHBoxLayout()

		espNameLineEdit = QtWidgets.QLineEdit()
		espNameLineEdit.setPlaceholderText('ESP Name')
		espNameLineEdit.textChanged.connect(lambda: espNameLineEdit.setStyleSheet('color : black;'))
		hbox.addWidget(espNameLineEdit)

		espIpLineEdit = QtWidgets.QLineEdit()
		espIpLineEdit.setPlaceholderText('ESP IP')
		espIpLineEdit.textChanged.connect(lambda: espIpLineEdit.setStyleSheet('color : black;'))
		hbox.addWidget(espIpLineEdit)

		deleteButton = QtWidgets.QToolButton()
		deleteButton.setIcon(_ui.style().standardIcon(QtWidgets.QStyle.SP_TrashIcon))
		hbox.addWidget(deleteButton)
		deleteButton.clicked.connect(self.removeEsp)

		if _ui.espVerticalLayout.rowCount() == 0:
			deleteButton.setEnabled(False)

		_ui.espVerticalLayout.addRow(hbox)
		self.updateAddEspButton()


	def removeEsp(self):
		"""Removes an ESP device record from the list of records.
		
		This function removes the selected ESP device record from the list of ESP devices.

		Args:
			self: An instance of this class.
		"""

		for i in range(_ui.espVerticalLayout.rowCount()):

			item = _ui.espVerticalLayout.itemAt(i, QtWidgets.QFormLayout.FieldRole).itemAt(2)

			if not item == None and _ui.sender() == item.widget():

				_ui.espVerticalLayout.removeRow(i)
				self.updateAddEspButton()
				break


	def updateAddEspButton(self):
		"""Updates the add ESP device button such that it is always placed below all records.

		This function firstly removes the add ESP device button from the list of records, and then adds it again to the bottom of the list to ensure it always remains below all records.

		Args:
			self: An instance of this class.
		"""

		self.removeAddEspButton()
		self.showAddEspButton()


	def removeAddEspButton(self):
		"""Removes the add ESP device button from the bottom of the list of records.
		
		This function removes the add ESP device button from the bottom of the list of ESP devices, to allow it to be added again later.

		Args:
			self: An instance of this class.
		"""

		for i in range(_ui.espVerticalLayout.rowCount()):

			item = _ui.espVerticalLayout.itemAt(i, QtWidgets.QFormLayout.FieldRole).itemAt(2)

			if item == None:

				_ui.espVerticalLayout.removeRow(i)
				break


	def showAddEspButton(self):
		"""Adds the add ESP device button to the bottom of the list of records.

		This function adds the add ESP device button to the bottom of the list of ESP devices, to allow the user to add another ESP device to the list. This function is called after the add ESP device button is removed from the list of records.

		Args:
			self: An instance of this class.
		"""

		hbox = QtWidgets.QHBoxLayout()

		addButton = QtWidgets.QToolButton()
		addButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		addButton.setIcon(QtGui.QIcon("./bin/sign-add-icon.png"))
		addButton.setText('  Add ESP Device')
		addButton.clicked.connect(self.addEsp)
		addButton.setAutoRaise(True)

		hbox.addWidget(addButton)
		_ui.espVerticalLayout.addRow(hbox)


	def browseSketchFiles(self):
		"""Displays a dialog window that allows the user to select an ino file to be uploaded to the ESP devices.

        Displays a dialog window that allows the user to select an ino file to be uploaded to the ESP devices. The path of the selected file is then copied into the sketch text box, before the directory of that sketch is copied into the directory text box.

        Args:
            self: An instance of this class.
		"""

		tempFile, _ = QtWidgets.QFileDialog.getOpenFileName(_ui, 'Sketch to Upload', QtCore.QDir.rootPath(), '*.ino')

		if tempFile != '' and tempFile != _ui.sketchLineEdit.text():
			_ui.sketchLineEdit.setStyleSheet('color : black;')
			_ui.sketchLineEdit.setText(tempFile)
			_ui.directoryLineEdit.setText(f'{os.path.dirname(os.path.realpath(tempFile))}/')


	def startUploadDialog(self):
		"""Starts the upload dialog window.

		This function initially checks that all fields in the current window are filled, before then initialising the upload dialog window and beigning the upload process.

		Args:
			self: An instance of this class.
		"""

		espNames = []
		espIps = []

		_ui.uploadLabelError.setText('')

		for i in range(_ui.espVerticalLayout.rowCount() - 1):
			espNameBox = _ui.espVerticalLayout.itemAt(i, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget()
			espIpBox = _ui.espVerticalLayout.itemAt(i, QtWidgets.QFormLayout.FieldRole).itemAt(1).widget()

			if not self.checkFieldIsEmpty(espNameBox):
				return

			if not self.checkFieldIsEmpty(espIpBox):
				return

			espNames.append(espNameBox.text())
			espIps.append(espIpBox.text())

		if not self.isNoDuplicates(espNames) or not self.isNoDuplicates(espIps):
			_ui.uploadLabelError.setStyleSheet('color : red;')
			_ui.uploadLabelError.setText('ESP devices must not contain duplicates.')

		if not self.checkFieldIsEmpty(_ui.deviceIpLineEdit):
			return

		if not self.checkFieldIsEmpty(_ui.udpPortLineEdit):
			return

		if not self.checkFieldIsEmpty(_ui.otaPortLineEdit):
			return

		if not self.checkFieldIsEmpty(_ui.sketchLineEdit):
			return

		uploadDialog = UploadDialogController()
		uploadDialog.setEspIps(espIps)
		uploadDialog.setEspDevices(espNames)
		uploadDialog.setIpOfSender(_ui.deviceIpLineEdit.text())
		uploadDialog.setUdpPort(_ui.udpPortLineEdit.text())
		uploadDialog.setOtaPort(_ui.otaPortLineEdit.text())
		uploadDialog.setIsTimed(_ui.testCheckbox.isChecked())
		uploadDialog.setIsVerbose(_ui.verboseCheckbox.isChecked())
		uploadDialog.setSketchAndDirectoryPath(_ui.sketchLineEdit.text(), _ui.directoryLineEdit.text())
		uploadDialog.startUpload()
		uploadDialog.exec_()

	def checkFieldIsEmpty(self, lineEdit):
		"""Checks if a field is empty.

		This function checks if a field is empty, and if it is, displays an error message.

		Args:
			self: An instance of this class.
			lineEdit: The line edit to check.

		Returns:
			True if the field is empty, False if it is not.
		"""

		if not lineEdit.text() or lineEdit.text() == 'Field must not be empty.':

				lineEdit.setText('Field must not be empty.')
				lineEdit.setStyleSheet('color : red;')
				return False

		return True


	def isNoDuplicates(self, list):
		"""Checks if a list contains duplicates.

		This function checks if a list contains duplicates. It is used for checking duplicates in the list of ESP names and IP addresses.

		Args:
			self: An instance of this class.
			list: The list to check.

		Returns:
			False if the list contains duplicates, True if it does not.
		"""

		seen = set()
		return not any(i in seen or seen.add(i) for i in list)
