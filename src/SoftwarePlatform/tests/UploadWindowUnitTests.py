import sys
import os
sys.path.append("..")
import unittest
from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import MainController

class TestMainUploadTabController(unittest.TestCase):

    def test_init(self):
        self.main = MainController.MainWindow()

        self.assertEqual(self.main.espVerticalLayout.rowCount(), 2)
        self.assertEqual(self.main.deviceIpLineEdit.text(), "")
        self.assertEqual(self.main.udpPortLineEdit.text(), "")
        self.assertEqual(self.main.otaPortLineEdit.text(), "")
        self.assertEqual(self.main.sketchLineEdit.text(), "")
        self.assertEqual(self.main.directoryLineEdit.text(), "")
        self.assertEqual(self.main.testCheckbox.isChecked(), False)
        self.assertEqual(self.main.verboseCheckbox.isChecked(), False)
        self.assertEqual(self.main.startButton.text(), "Start")

    def test_all_empty(self):
        self.main = MainController.MainWindow()

        QTest.mouseClick(self.main.startButton, Qt.LeftButton)

        self.assertEqual(self.main.espVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().text(), 'Field must not be empty.')

    def test_empty_esp_ip(self):
        self.main = MainController.MainWindow()

        self.main.espVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().setText('esp1')

        QTest.mouseClick(self.main.startButton, Qt.LeftButton)

        self.assertEqual(self.main.espVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(1).widget().text(), 'Field must not be empty.')

    def test_empty_ip(self):
        self.main = MainController.MainWindow()

        self.main.espVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().setText('esp1')
        self.main.espVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(1).widget().setText('esp1.local')

        QTest.mouseClick(self.main.startButton, Qt.LeftButton)

        self.assertEqual(self.main.deviceIpLineEdit.text(), 'Field must not be empty.')

    def test_empty_udp(self):
        self.main = MainController.MainWindow()

        self.main.espVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().setText('esp1')
        self.main.espVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(1).widget().setText('esp1.local')
        self.main.deviceIpLineEdit.setText('192.168.1.114')

        QTest.mouseClick(self.main.startButton, Qt.LeftButton)

        self.assertEqual(self.main.udpPortLineEdit.text(), 'Field must not be empty.')

    def test_empty_ota(self):
        self.main = MainController.MainWindow()

        self.main.espVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().setText('esp1')
        self.main.espVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(1).widget().setText('esp1.local')
        self.main.deviceIpLineEdit.setText('192.168.1.114')
        self.main.udpPortLineEdit.setText('7375')

        QTest.mouseClick(self.main.startButton, Qt.LeftButton)

        self.assertEqual(self.main.otaPortLineEdit.text(), 'Field must not be empty.')

    def test_empty_sketch(self):
        self.main = MainController.MainWindow()

        self.main.espVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().setText('esp1')
        self.main.espVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(1).widget().setText('esp1.local')
        self.main.deviceIpLineEdit.setText('192.168.1.114')
        self.main.udpPortLineEdit.setText('7375')
        self.main.otaPortLineEdit.setText('3232')

        QTest.mouseClick(self.main.startButton, Qt.LeftButton)

        self.assertEqual(self.main.sketchLineEdit.text(), 'Field must not be empty.')

    def test_add_esp(self):
        self.main = MainController.MainWindow()

        self.assertEqual(self.main.espVerticalLayout.rowCount(), 2)
        QTest.mouseClick(self.main.espVerticalLayout.itemAt(1, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget(), Qt.LeftButton)
        self.assertEqual(self.main.espVerticalLayout.rowCount(), 3)

    def test_remove_esp(self):
        self.main = MainController.MainWindow()

        self.assertEqual(self.main.espVerticalLayout.rowCount(), 2)
        QTest.mouseClick(self.main.espVerticalLayout.itemAt(1, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget(), Qt.LeftButton)
        self.assertEqual(self.main.espVerticalLayout.rowCount(), 3)
        QTest.mouseClick(self.main.espVerticalLayout.itemAt(1, QtWidgets.QFormLayout.FieldRole).itemAt(2).widget(), Qt.LeftButton)
        self.assertEqual(self.main.espVerticalLayout.rowCount(), 2)

    def test_dir_auto_fill(self):
        self.main = MainController.MainWindow()

        self.main.sketchLineEdit.setText('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/OTA_LoRa_Sync/OTA_LoRa_Sync.ino')
        self.main.directoryLineEdit.setText(f'{os.path.dirname(os.path.realpath(self.main.sketchLineEdit.text()))}/')
        self.assertEqual(self.main.directoryLineEdit.text(), f'/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/OTA_LoRa_Sync/')


if __name__ == '__main__':
    unittest.main()