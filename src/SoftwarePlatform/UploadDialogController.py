"""This module handles the control of the upload dialog window.

Once the user has selected to upload a sketch, the upload dialog window is opened and this module is initialised to handle the control of the window.

    Typical usage example:

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
"""

from ui_py.UploadDialog import Ui_Dialog
from SaveFormController import SaveFormController
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QThread
from BatchUploadWorker import BatchUploadWorker

import time

class UploadDialogController(QtWidgets.QDialog, Ui_Dialog):
	"""Handles the operations of the upload dialog window.

	This class handles the operations of the upload dialog window, including the initialisation of its user interface components, the creation of a separate thread to handle the batch upload process, and the handling of updates to the user interface when the upload is in progress.

	Attributes:
		_espIps: A list of ESP IP addresses to upload to.
		_espDevices: A list of ESP device names used to update DNS in the Arduino sketch.
		_ipOfSender: The IP address of the device that is sending the sketch.
		_udpPort: The UDP port to use for communicationg with the ESP devices.
		_otaPort: The OTA port to use for the over-the-air uploading of sketches.
		_sketchPath: The path to the sketch to upload.
		_sketchDirectory: The directory of the sketch.
		_isTimed: Whether or not the upload should time synchronisation once it is complete.
		_isVerbose: Whether or not to display verbose output.
	"""

	_espIps = []
	_espDevices = []

	_ipOfSender = ''
	_udpPort = 0
	_otaPort = 0

	_sketchPath = ''
	_sketchDirectory = ''

	_isTimed = False
	_isVerbose = False

	def __init__(self, *args, obj=None, **kwargs):
		"""Initialises an instance of this class.

		This function initialises an instance of this class and calls the user interface components to be initialised.

		Args:
            self: An instance of this class.
            *args: Arguments passed to the constructor.
            obj: An object passed to the constructor.
            **kwargs: Keyword arguments passed to the constructor.
		"""

		super(UploadDialogController, self).__init__(*args, **kwargs)

		self.setupUi(self)
		self.initUiComponents()


	def initUiComponents(self):
		"""Initialises the user interface components.
		
		This function initialises the user interface components by setting the progress bar to initially be 0, and by setting what functions should be called when cancel/save are clicked.

		Args:
			self: An instance of this class.
		"""

		self.uploadProgressBar.setValue(0)
		self.uploadButtonBox.accepted.connect(self.onSaveButtonClicked)
		self.uploadButtonBox.rejected.connect(self.onCancelButtonClicked)


	def startUpload(self):
		"""Starts the upload process.

		This function starts the upload process by creating a separate thread to handle the batch upload process, and passing any necessary data to it. It also creates processes with the worker thread to allow the thread to communicate specific upload progress updates to the user interface.

		Args:
			self: An instance of this class.
		"""

		self.threadFinished = False
		self.uploadButtonBox.buttons()[0].setEnabled(False)

		self.count = 0
		self.flag = False
		self.timerLabel.setText('Timer: Not Started')

		self.timer = QTimer(self)
		self.timer.timeout.connect(self.showTime)

		self.thread = QThread()

		self.worker = BatchUploadWorker(self.progressBarLabel, _espIps, _espDevices, _ipOfSender, int(_udpPort), int(_otaPort), _sketchPath, _sketchDirectory, _isTimed, _isVerbose)

		self.worker.moveToThread(self.thread)

		self.thread.started.connect(self.worker.runUpload)
		self.worker.finished.connect(self.finished)
		self.worker.finished.connect(self.thread.quit)
		self.worker.finished.connect(self.worker.deleteLater)
		self.thread.finished.connect(self.thread.deleteLater)
		self.worker.timerStart.connect(self.startTimer)
		self.worker.timerStop.connect(self.stopTimer)
		self.worker.progressUpdate.connect(self.updateProgressBar)
		self.worker.labelUpdate.connect(self.updateDebugLabel)
		self.worker.outputUpdate.connect(self.updateOutputBox)

		self.thread.start()


	def startTimer(self):
		"""Starts the timer.

		This function starts the timer by setting the flag to True, and starting the timer.

		Args:
			self: An instance of this class.
		"""

		self.flag = True
		self.timer.start(100)


	def stopTimer(self):
		"""Stops the timer.

		This function stops the timer by setting the flag to False, and stopping the timer. At this point, the save button is now enabled as a result has been received.

		Args:
			self: An instance of this class.
		"""

		self.flag = False
		self.timer.stop()
		self.uploadButtonBox.buttons()[0].setEnabled(True)


	def showTime(self):
		"""Updates the time within the timer text box.
		
		This function updates the time within the timer text box by incrementing the count by 1, and displaying a timer output in the format of seconds.milliseconds.

		Args:
			self: An instance of this class.
		"""

		if self.flag:
			self.count += 1

		text = f'Timer: {str(self.count / 10)}'
		self.timerLabel.setText(text)


	def updateProgressBar(self, value, isMod):
		"""Updates the value of the progress bar.

		This function updates the value of the progress bar by setting it to the value passed in. If the isMod flag is set to True, the progress bar is set to the value passed in + 1 to ensure that it reaches 100%, otherwise the progress bar is incremented by the value passed in.

		Args:
			self: An instance of this class.
			value: The value to set the progress bar to.
			isMod: Whether or not to set the progress bar to the value passed in + 1.
		"""

		oldValue = self.uploadProgressBar.value()

		if not isMod:
			value += 1

		for i in range(oldValue, oldValue + value):
			time.sleep(0.05)
			self.uploadProgressBar.setValue(i)


	def updateDebugLabel(self, message):
		"""Updates the debug label.

		This function updates the debug label by setting it to the message passed in.

		Args:
			self: An instance of this class.
			message: The message to set the debug label to.
		"""

		self.progressBarLabel.setText(message)


	def updateOutputBox(self, message):
		"""Updates the output text box.

		This function updates the output text box by appending to it the message passed in.

		Args:
			self: An instance of this class.
			message: The message to append to the output text box.
		"""

		self.outputBox.append(message)


	def setEspIps(self, nEspIps):
		"""Sets the ESP IPs.

		This function sets the ESP IPs to the value passed in and assigns a False to them which is used to identify if they have acknowledged a sent message in the upload process.

		Args:
			self: An instance of this class.
			nEspIps: The new ESP IPs.
		"""

		global _espIps

		_espIps = []

		for espIp in nEspIps:
			_espIps.append([espIp, False])


	def setEspDevices(self, nEspDevices):
		"""Sets the ESP names.

		This function sets the ESP names to the value passed in.

		Args:
			self: An instance of this class.
			nEspDevices: The new ESP names.
		"""

		global _espDevices
		_espDevices = nEspDevices


	def setIpOfSender(self, nIpOfSender):
		"""Sets the IP of the sender.

		This function sets the IP of the sender to the value passed in.

		Args:
			self: An instance of this class.
			nIpOfSender: The new IP of the sender.
		"""

		global _ipOfSender
		_ipOfSender = nIpOfSender


	def setUdpPort(self, nUdpPort):
		"""Sets the UDP port.

		This function sets the UDP port to the value passed in.

		Args:
			self: An instance of this class.
			nUdpPort: The new UDP port.
		"""

		global _udpPort
		_udpPort = nUdpPort


	def setOtaPort(self, nOtaPort):
		"""Sets the OTA port.

		This function sets the OTA port to the value passed in.
		
		Args:
			self: An instance of this class.
			nOtaPort: The new OTA port.
		"""

		global _otaPort
		_otaPort = nOtaPort


	def setIsTimed(self, nIsTimed):
		"""Sets the isTimed flag.

		This function sets the isTimed flag to the value passed in.

		Args:
			self: An instance of this class.
			nIsTimed: The new isTimed flag.		
		"""

		global _isTimed
		_isTimed = nIsTimed


	def setIsVerbose(self, nIsVerbose):
		"""Sets the isVerbose flag.
		
		This function sets the isVerbose flag to the value passed in.
		
		Args:
			self: An instance of this class.
			nIsVerbose: The new isVerbose flag.
		"""

		global _isVerbose
		_isVerbose = nIsVerbose


	def setSketchAndDirectoryPath(self, nSketchPath, nSketchDirectory):
		"""Sets the sketch and sketch directory paths.

		This function sets the sketch and sketch directory paths to the values passed in.

		Args:
			self: An instance of this class.
			nSketchPath: The new sketch path.
			nSketchDirectory: The new sketch directory path.
		"""

		global _sketchPath, _sketchDirectory
		_sketchPath, _sketchDirectory = nSketchPath, nSketchDirectory


	def onCancelButtonClicked(self):
		"""Cancels the upload process.

		This function cancels the upload process when the cancel button is clicked.

		Args:
			self: An instance of this class.
		"""

		self.stopWorker()


	def onSaveButtonClicked(self):
		"""Launches the save result dialog window.

		This function launches the save result dialog window when the save button is clicked.

		Args:
			self: An instance of this class.
		"""

		self.showSaveDialog()


	def showSaveDialog(self):
		"""Shows the save result dialog window.
		
		This function shows the save result dialog window and sends the result to that dialog.

		Args:
			self: An instance of this class.
		"""

		saveDialog = SaveFormController()
		saveDialog.specifyResult(self.timerLabel.text().split(':')[1].lstrip())
		saveDialog.exec_()
		if saveDialog.getSaved():
			self.uploadButtonBox.buttons()[0].setEnabled(False)


	def stopWorker(self):
		"""Stops the upload worker class and thread.

		This function stops the upload worker class and thread should the cancel button be clicked.

		Args:
			self: An instance of this class.
		"""
		
		self.worker.kill()
		self.thread.quit()
		while self.thread.isRunning():
			pass
		self.close()


	def finished(self):
		"""Disables the cancel button.

		This function disables the cancel button when the upload worker class finishes.

		Args:
			self: An instance of this class.
		"""

		self.uploadButtonBox.buttons()[1].setEnabled(False)