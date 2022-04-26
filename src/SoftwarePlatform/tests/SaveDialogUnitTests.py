import sys
import os
sys.path.append("..")
import unittest
from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from MainController import MainWindow
from SaveFormController import SaveFormController

class TestSaveDialogController(unittest.TestCase):

    def test_init(self):
        self.main = MainWindow()
        self.save = SaveFormController()
        self.save.specifyResult('128.7')

        self.assertEqual(self.save.labelResult.text(), 'Result: 128.7')
        self.assertEqual(self.save.filenameLineEdit.text(), '')
        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 1)

    def test_save_result_empty_file(self):

        path = '/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/empty_save.txt'
        if os.path.getsize(path) != 0:
            open(path, 'w').close()

        self.main = MainWindow()
        self.save = SaveFormController()
        self.save.specifyResult('128.7')
        self.save.filenameLineEdit.setText(path)
        QTest.mouseClick(self.save.buttonBox.buttons()[0], Qt.LeftButton)

    def test_add_record(self):
        self.main = MainWindow()
        self.save = SaveFormController()
        self.save.specifyResult('128.7')

        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 1)

        QTest.mouseClick(self.save.recordVerticalLayout.itemAt(0).itemAt(0).widget(), Qt.LeftButton)
        
        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 2)

    def test_remove_record(self):
        self.main = MainWindow()
        self.save = SaveFormController()
        self.save.specifyResult('128.7')

        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 1)

        QTest.mouseClick(self.save.recordVerticalLayout.itemAt(0).itemAt(0).widget(), Qt.LeftButton)
        
        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 2)

        QTest.mouseClick(self.save.recordVerticalLayout.itemAt(0).itemAt(2).widget(), Qt.LeftButton)

        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 1)

    def test_empty_param(self):
        self.main = MainWindow()
        self.save = SaveFormController()
        self.save.specifyResult('128.7')

        QTest.mouseClick(self.save.recordVerticalLayout.itemAt(0).itemAt(0).widget(), Qt.LeftButton)

        self.save.filenameLineEdit.setText('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/empty_save.txt')
        QTest.mouseClick(self.save.buttonBox.buttons()[0], Qt.LeftButton)
        self.assertEqual(self.save.recordVerticalLayout.itemAt(0).itemAt(0).widget().text(), 'Field must not be empty.')

    def test_empty_value(self):
        self.main = MainWindow()
        self.save = SaveFormController()
        self.save.specifyResult('128.7')

        QTest.mouseClick(self.save.recordVerticalLayout.itemAt(0).itemAt(0).widget(), Qt.LeftButton)

        self.save.filenameLineEdit.setText('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/empty_save.txt')
        self.save.recordVerticalLayout.itemAt(0).itemAt(0).widget().setText('Min Boost')
        QTest.mouseClick(self.save.buttonBox.buttons()[0], Qt.LeftButton)
        self.assertEqual(self.save.recordVerticalLayout.itemAt(0).itemAt(1).widget().text(), 'Field must not be empty.')

    def test_line_length_error(self):
        self.main = MainWindow()
        self.save = SaveFormController()
        self.save.specifyResult('128.7')
        self.save.filenameLineEdit.setText('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/empty_save.txt')

        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 1)

        QTest.mouseClick(self.save.recordVerticalLayout.itemAt(0).itemAt(0).widget(), Qt.LeftButton)
        
        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 2)

        self.save.recordVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().setText('Min Boost')
        self.save.recordVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(1).widget().setText('200')

        QTest.mouseClick(self.save.buttonBox.buttons()[0], Qt.LeftButton)

        self.assertEqual(self.save.labelError.text(), 'Number of parameters do not match length of line 1.')

    def test_param_error(self):
        self.main = MainWindow()
        self.save = SaveFormController()
        self.save.specifyResult('128.7')
        self.save.filenameLineEdit.setText('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/param_error.txt')

        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 1)

        QTest.mouseClick(self.save.recordVerticalLayout.itemAt(0).itemAt(0).widget(), Qt.LeftButton)
        
        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 2)

        self.save.recordVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().setText('Max Boost')
        self.save.recordVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(1).widget().setText('2500')

        QTest.mouseClick(self.save.buttonBox.buttons()[0], Qt.LeftButton)

        self.assertEqual(self.save.recordVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().text(), 'Param not in log file, line 1.')

    def test_result_error(self):
        self.main = MainWindow()
        self.save = SaveFormController()
        self.save.specifyResult('128.7')
        self.save.filenameLineEdit.setText('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/result_error.txt')

        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 1)

        QTest.mouseClick(self.save.recordVerticalLayout.itemAt(0).itemAt(0).widget(), Qt.LeftButton)
        
        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 2)

        self.save.recordVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().setText('Min Boost')
        self.save.recordVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(1).widget().setText('200')

        QTest.mouseClick(self.save.buttonBox.buttons()[0], Qt.LeftButton)

        self.assertEqual(self.save.labelError.text(), 'Result not found in line 1.')

    def test_correct_save(self):
        self.main = MainWindow()
        self.save = SaveFormController()
        self.save.specifyResult('128.7')
        self.save.filenameLineEdit.setText('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/param_error.txt')

        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 1)

        QTest.mouseClick(self.save.recordVerticalLayout.itemAt(0).itemAt(0).widget(), Qt.LeftButton)
        
        self.assertEqual(self.save.recordVerticalLayout.rowCount(), 2)

        self.save.recordVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(0).widget().setText('Min Boost')
        self.save.recordVerticalLayout.itemAt(0, QtWidgets.QFormLayout.FieldRole).itemAt(1).widget().setText('200')

        QTest.mouseClick(self.save.buttonBox.buttons()[0], Qt.LeftButton)

if __name__ == "__main__":
    unittest.main()