"""This module acts as the worker class to perform the batch upload and timing of convergence of an Arduino sketch to ESP devices.

Once this module has been instantiated by the upload dialog, the upload process is started in a separate thread to the user interface thread. This worker class is responsible for performing the upload process and feeding information back to the UploadDialogController to ensure that the user is notified of the progress of the upload and timing process.

    Typical usage example:

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
"""

import os
import socket
import subprocess
import time
from sys import platform

from PyQt5.QtCore import QObject, pyqtSignal
from AnimatedLoadText import Loader

_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
_sock.settimeout(5.0)

class BatchUploadWorker(QObject):
    """Performs the batch upload and timing of convergence of an Arduino sketch to ESP devices.
    
    This function is responsible for performing the batch upload and timing of convergence of an Arduino sketch to ESP devices. When progress is made during the process, this class sends signals to the UploadDialogController to update the user interface.

    Attributes:
        _espIps: A list of ESP IP addresses to upload to.
		_espDevices: A list of ESP device names used to update DNS in the Arduino sketch.
		_ipOfSender: The IP address of the device that is sending the sketch.
		_udpPort: The UDP port to use for communicationg with the ESP devices.
		_otaPort: The OTA port to use for the over-the-air uploading of sketches.
		_sketchPath: The path to the sketch to upload.
		_sketchDirectory: The directory of the sketch.
		_isTimed: Whether or not the upload should time convergence once it is complete.
		_isVerbose: Whether or not to display verbose output.

        finished = pyqtSignal(): A signal to be emitted when the upload process is complete.
        timerStart = pyqtSignal(): A signal to be emitted when the timer should be started.
        timerStop = pyqtSignal(): A signal to be emitted when the timer should be stopped.
        progressUpdate = pyqtSignal(int, bool): A signal to be emitted when the progress of the upload process is updated.
        labelUpdate = pyqtSignal(str): A signal to be emitted when the debug label should be updated.
        outputUpdate = pyqtSignal(str): A signal to be emitted when the output text box should be updated.
    """

    _espIps = []
    _espDevices = []

    _ipOfSender = ''
    _udpPort = 0
    _otaPort = 0

    _sketchPath = ''
    _sketchDirectory = ''
    _binFile = ''

    _isTimed = False
    _isVerbose = False

    finished = pyqtSignal()
    timerStart = pyqtSignal()
    timerStop = pyqtSignal()
    progressUpdate = pyqtSignal(int, bool)
    labelUpdate = pyqtSignal(str)
    outputUpdate = pyqtSignal(str)


    def __init__(self, progressBarLabel, nEspIps, nEspDevices, nIpOfSender, nUdpPort, nOtaPort, nSketchPath, nSketchDirectory, nIsTimed, nIsVerbose):
        """Initialises the worker class for the upload process.

        This function is responsible for initialising the worker class for the upload process. It is responsible for setting class attributes and determining the size of increments to be added to the user interface's progress bar.

        Args:
            progressBarLabel: The progress bar label to update with progress information.
            nEspIps: A list of ESP IP addresses to upload to.
            nEspDevices: A list of ESP device names used to update DNS in the Arduino sketch.
            nIpOfSender: The IP address of the device that is sending the sketch.
            nUdpPort: The UDP port to use for communicationg with the ESP devices.
            nOtaPort: The OTA port to use for the over-the-air uploading of sketches.
            nSketchPath: The path to the sketch to upload.
            nSketchDirectory: The directory of the sketch.
            nIsTimed: Whether or not the upload should time convergence once it is complete.
            nIsVerbose: Whether or not to display verbose output.
        """

        super().__init__()

        global _espIps, _espDevices, _ipOfSender, _udpPort, _otaPort, _sketchPath, _sketchDirectory, _binFile, _isTimed, _isVerbose

        _espIps, _espDevices, _ipOfSender, _udpPort, _otaPort, _sketchPath, _sketchDirectory, _isTimed, _isVerbose = nEspIps, nEspDevices, nIpOfSender, nUdpPort, nOtaPort, nSketchPath, nSketchDirectory, nIsTimed, nIsVerbose

        _binFile = f'{_sketchPath}.bin'

        self.isKilled = False
        self.progressBarLabel = progressBarLabel

        self.ipIncrements = int(21 / len(_espIps))
        self.ipMod = 21 % len(_espIps)

        if _isTimed:
            self.espIncrements = int(61 / len(_espDevices))
            self.espMod = 61 % len(_espDevices)
        else:
            self.espIncrements = int(81 / len(_espDevices))
            self.espMod = 81 % len(_espDevices)
        

    def falsifyUdpResponses(self):
        """Falsifies the UDP responses from the ESP devices.
        
        This function is responsible for falsifying the UDP responses from the ESP devices. In effect, it sets the boolean value associated with each ESP IP address to False to allow the next round of UDP messages to be sent and wait for an acknowledgement.
        
        Args:
            self: The class instance.
        """

        for ip in _espIps:
            ip[1] = False


    def runUpload(self):
        """Runs the upload process.

        This function is responsible for running the upload process and does this by calling all the necessary processes needed to complete the upload and time the convergence if desired. It is also responsible for sending signals to the UploadDialogController to update the user interface. After the completion of each process, this funtion makes a check that the previous function was completed successfully before beginning the next one.

        Args:
            self: The class instance.
        """

        self.falsifyUdpResponses()

        self.outputUpdate.emit('--- Pinging ESP Devices ---\n')

        if self.pingDevices() and not self.isKilled:

            self.progressUpdate.emit(self.ipMod, True)
            self.outputUpdate.emit(f'\n--- Uploading Sketch to Devices ---\n')

            if not self.uploadSketch() or self.isKilled:

                self.outputUpdate.emit('Upload Failed. Process terminated early.')

            elif not _isTimed:

                self.outputUpdate.emit('✓ Upload Complete')

            else:

                self.progressUpdate.emit(self.espMod, True)
                self.falsifyUdpResponses()
                self.outputUpdate.emit(f'\n--- Starting Devices ---\n')

                if self.startDevices() and not self.isKilled:

                    self.progressUpdate.emit(self.ipMod, True)
                    self.timerStart.emit()
                    self.falsifyUdpResponses()

                    self.outputUpdate.emit(f'\n--- Waiting for Devices to Converge ---\n')
                    self.waitForConvergence()
        
        self.finished.emit()


    def pingDevices(self):
        """Pings the ESP devices.

        This function is responsible for pinging the ESP devices. It sends each ESP device a ping message and waits for an acknowledgement. The pinging of a device occurs until an acknowledgement is received or a ping message has failed 10 times, at which point False is returned.

        Args:
            self: The class instance.

        Returns:
            True if all the ESP devices are pinged successfully, False otherwise.
        """

        for ip in _espIps:

            self.loader = Loader(self.progressBarLabel, f'Pinging {ip[0]}...', '').start()

            i = 0

            while i < 10 and not ip[1] and not self.isKilled:

                try:

                    _sock.sendto(bytes("Ping", 'utf-8'), (ip[0], _udpPort))
                    return_data, return_ip = _sock.recvfrom(4096)
                    response = return_data.decode("utf-8")

                    if return_ip[0] == socket.gethostbyname(ip[0]) and response == "Received":
                        if _isVerbose:
                            self.outputUpdate.emit(f'Message: {response}\n from: {return_ip}\n')
                        ip[1] = True
                    
                except socket.timeout as time_e:
                    if _isVerbose:
                        self.outputUpdate.emit(str(time_e))

                except socket.error as err_e:
                    if _isVerbose:
                        self.outputUpdate.emit(str(err_e))

                i += 1

            if ip[1]:
                self.loader.stop()
                self.outputUpdate.emit(f'✓ Pinged {ip[0]} Successfully')
                self.progressUpdate.emit(self.ipIncrements, False)
            else:
                self.loader.stop()
                self.outputUpdate.emit(f'✘ Pinging {ip[0]} Failed')
                return False

        return True


    def uploadSketch(self):
        """Uploads the sketch to the ESP devices.

        This function is responsible for uploading the sketch to the ESP devices. It first edits the DNS name in the sketch to be the name of the ESP device being uploaded to before compiling it into a bin file using Arduino's command line interface. It then attempts to upload the sketch to the ESP device using the espota script from Espressif. It then checks that the upload was successful before returning True. It will try 10 times for a successful upload before returning False. This loop is carried out for each specific ESP device.

        Args:
            self: The class instance.

        Returns:
            True if all the ESP devices are uploaded to successfully, False otherwise.
        """

        for index, esp in enumerate(_espDevices, start = 0):

            if not self.isKilled:
                self.loader = Loader(self.progressBarLabel, f'Uploading sketch to {esp} - {_espIps[index][0]}...', '').start()

                if platform.startswith('linux'):
                    subprocess.call(f"sed -i -e 's/#define DNS.*/#define DNS \"{esp}\"/' {_sketchPath}", shell=True)
                elif platform.startswith('win32'):
                    subprocess.call(f'{os.getcwd()}/bin/GnuWin32/bin/sed -i -e "s/#define DNS.*/#define DNS \\\"{esp}\\\"/" {_sketchPath}', shell=True)

                subprocess.run([f'arduino-cli compile --fqbn esp32:esp32:esp32 {_sketchPath} --output-dir {_sketchDirectory}'], shell=True)

                returnCode = 1
                j = 0

                while returnCode == 1 and j < 10 and not self.isKilled:

                    cmd = f'python bin/espota.py -i {_espIps[index][0]} -I {_ipOfSender} -p {_otaPort} -P {_otaPort} -f {_binFile}'

                    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                    if _isVerbose:
                        self.outputUpdate.emit(cmd)
                        for line in p.stdout.readlines():
                            self.outputUpdate.emit(str(line))

                    p.wait()
                    time.sleep(10)

                    returnCode = p.returncode

                    j += 1

                if returnCode == 1:
                    self.outputUpdate.emit(f'✘ Sketch Upload to {esp} - {_espIps[index][0]} Failed')
                    self.loader.stop()
                    return False
                else:
                    self.progressUpdate.emit(self.espIncrements, False)
                    self.outputUpdate.emit(f'✓ Sketch Uploaded to {esp} - {_espIps[index][0]} Successfully')
                    self.loader.stop()

        if not _isTimed:
            self.labelUpdate.emit('Uploads Completed Successfully.')
        return True


    def startDevices(self):
        """Starts the ESP devices.

        This function is responsible for starting the ESP devices. It sends each ESP device a start message and waits for an acknowledgement. The attempt to start a device occurs until an acknowledgement is received or a start message has failed 10 times, at which point False is returned.

        Args:
            self: The class instance.

        Returns:
            True if all the ESP devices are started successfully, False otherwise.
        """

        for index, ip in enumerate(_espIps, start = 0):

            self.loader = Loader(self.progressBarLabel, f'Starting {_espDevices[index]} - {ip[0]}...', '').start()

            i = 0

            while i < 10 and not ip[1] and not self.isKilled:

                try:

                    _sock.sendto(bytes("Start", 'utf-8'), (ip[0], _udpPort))
                    return_data, return_ip = _sock.recvfrom(4096)
                    response = return_data.decode("utf-8")

                    if return_ip[0] == socket.gethostbyname(ip[0]) and response == 'Started':
                        if _isVerbose:
                            self.outputUpdate.emit(f'Message: {response}\n from: {return_ip}\n')
                        ip[1] = True
                        time.sleep(2)
                        
                except socket.timeout as time_e:
                    if _isVerbose:
                        self.outputUpdate.emit(str(time_e))

                except socket.error as err_e:
                    if _isVerbose:
                        self.outputUpdate.emit(str(err_e))

                i += 1

            if ip[1]:
                self.loader.stop()
                self.outputUpdate.emit(f'✓ {_espDevices[index]} - {ip[0]} Started Successfully')
                self.progressUpdate.emit(self.ipIncrements, False)
            else:
                self.loader.stop()
                self.outputUpdate.emit(f'✘ Starting {_espDevices[index]} - {ip[0]} Failed')
                return False

        return True


    def waitForConvergence(self):
        """Waits for the ESP devices to converge.

        This function will send a UDP message to each ESP device indefinitely until those ESP devices respond to say that they have converged. This function can be terminated using the cancel button in the GUI.

        Args:
            self: The class instance.
        """

        self.loader = Loader(self.progressBarLabel, 'Waiting for Devices to Converge...', 'Devices Converged Successfully.').start()

        while (not all(ping for (_, ping) in _espIps)) and not self.isKilled:

            for index, ip in enumerate(_espIps, start = 0):

                if not ip[1]:

                    try:
                                     
                        _sock.sendto(bytes("Sync", 'utf-8'), (ip[0], _udpPort))
                        return_data, return_ip = _sock.recvfrom(4096)
                        response = return_data.decode("utf-8")

                        if return_ip[0] == socket.gethostbyname(ip[0]) and response == 'Done':
                            if _isVerbose:
                                self.outputUpdate.emit(f'Message: {response}\n from: {return_ip}\n')
                            ip[1] = True
                            self.outputUpdate.emit(f'{_espDevices[index]} - {ip[0]} Done!')

                    except socket.timeout as time_e:
                        if _isVerbose:
                            self.outputUpdate.emit(str(time_e))

                    except socket.error as err_e:
                        if _isVerbose:
                            self.outputUpdate.emit(str(err_e))

        self.timerStop.emit()
        self.loader.stop()
        self.outputUpdate.emit('\n✓ Devices Converged Successfully!')


    def kill(self):
        """Kills the upload process.

        This function stops the animated text in the GUI and kills the upload process by setting the isKilled flag to True. This will allow a process to complete before quitting the process.

        Args:
            self: The class instance.
        """

        self.loader.cancel()
        while not self.loader.getFinished():
            pass
        self.isKilled = True
