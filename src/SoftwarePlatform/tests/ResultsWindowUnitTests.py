import sys
sys.path.append("..")
import unittest
from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import MainController

class TestMainResultsTabController(unittest.TestCase):

    def test_init(self):
        self.main = MainController.MainWindow()

        self.assertEqual(self.main.resultFileLineEdit.text(), '')
        self.assertEqual(self.main.gridLayout.rowCount(), 1)
        self.assertEqual(self.main.paramsGrid.rowCount(), 1)
        self.assertEqual(self.main.gridLayout.columnCount(), 1)
        self.assertEqual(self.main.paramsGrid.columnCount(), 1)
        self.assertEqual(self.main.comboBox.count(), 0)

    def test_empty_file(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/empty_timings.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        self.assertEqual(self.main.gridLayout.rowCount(), 1)
        self.assertEqual(self.main.paramsGrid.rowCount(), 1)
        self.assertEqual(self.main.gridLayout.columnCount(), 1)
        self.assertEqual(self.main.paramsGrid.columnCount(), 1)
        self.assertEqual(self.main.comboBox.count(), 0)
        self.assertEqual(self.main.loadErrorLabel.text(), 'File is empty.')

    def test_last_param_error(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/last_param_error.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        self.assertEqual(self.main.gridLayout.rowCount(), 1)
        self.assertEqual(self.main.paramsGrid.rowCount(), 1)
        self.assertEqual(self.main.gridLayout.columnCount(), 1)
        self.assertEqual(self.main.paramsGrid.columnCount(), 1)
        self.assertEqual(self.main.comboBox.count(), 0)
        self.assertEqual(self.main.loadErrorLabel.text(), 'RESULT parameter should appear last on Line 1.')

    def test_line_length_error(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/line_length_error.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        self.assertEqual(self.main.gridLayout.rowCount(), 1)
        self.assertEqual(self.main.paramsGrid.rowCount(), 1)
        self.assertEqual(self.main.gridLayout.columnCount(), 1)
        self.assertEqual(self.main.paramsGrid.columnCount(), 1)
        self.assertEqual(self.main.comboBox.count(), 0)
        self.assertEqual(self.main.loadErrorLabel.text(), 'Number of parameters in Line 2 does not match Line 1.')

    def test_param_match_error(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/param_match_error.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        self.assertEqual(self.main.gridLayout.rowCount(), 1)
        self.assertEqual(self.main.paramsGrid.rowCount(), 1)
        self.assertEqual(self.main.gridLayout.columnCount(), 1)
        self.assertEqual(self.main.paramsGrid.columnCount(), 1)
        self.assertEqual(self.main.comboBox.count(), 0)
        self.assertEqual(self.main.loadErrorLabel.text(), 'A parameter in Line 2 does not match the parameters Line 1.')

    def test_param_float_error(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/param_float_error.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        self.assertEqual(self.main.gridLayout.rowCount(), 1)
        self.assertEqual(self.main.paramsGrid.rowCount(), 1)
        self.assertEqual(self.main.gridLayout.columnCount(), 1)
        self.assertEqual(self.main.paramsGrid.columnCount(), 1)
        self.assertEqual(self.main.comboBox.count(), 0)
        self.assertEqual(self.main.loadErrorLabel.text(), 'Value of a parameter in Line 1 is not a float.')

    def test_correct_subplots(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/timings.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        self.assertEqual(self.main.gridLayout.count(), 5)
        self.assertEqual(self.main.gridLayout.itemAt(0).itemAt(1).widget().figure.get_axes()[0].get_xlabel(), 'MIN BOOST')
        self.assertEqual(self.main.gridLayout.itemAt(1).itemAt(1).widget().figure.get_axes()[0].get_xlabel(), 'MAX BOOST')
        self.assertEqual(self.main.gridLayout.itemAt(2).itemAt(1).widget().figure.get_axes()[0].get_xlabel(), 'PERIOD (SECONDS)')
        self.assertEqual(self.main.gridLayout.itemAt(3).itemAt(1).widget().figure.get_axes()[0].get_xlabel(), 'SYNC WINDOW')
        self.assertEqual(self.main.gridLayout.itemAt(4).itemAt(1).widget().figure.get_axes()[0].get_xlabel(), 'NUM DEVICES')

    def test_correct_checkboxes(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/timings.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        self.assertEqual(self.main.paramsGrid.itemAt(0).widget().text(), 'MIN BOOST')
        self.assertEqual(self.main.paramsGrid.itemAt(1).widget().text(), 'MAX BOOST')
        self.assertEqual(self.main.paramsGrid.itemAt(2).widget().text(), 'PERIOD (SECONDS)')
        self.assertEqual(self.main.paramsGrid.itemAt(3).widget().text(), 'SYNC WINDOW')
        self.assertEqual(self.main.paramsGrid.itemAt(4).widget().text(), 'NUM DEVICES')

    def test_correct_combobox(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/timings.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        self.assertGreater(self.main.comboBox.findText('ALL'), -1)
        self.assertGreater(self.main.comboBox.findText('MIN BOOST'), -1)
        self.assertGreater(self.main.comboBox.findText('MAX BOOST'), -1)
        self.assertGreater(self.main.comboBox.findText('PERIOD (SECONDS)'), -1)
        self.assertGreater(self.main.comboBox.findText('SYNC WINDOW'), -1)
        self.assertGreater(self.main.comboBox.findText('NUM DEVICES'), -1)
        self.assertGreater(self.main.comboBox.findText('NONE'), -1)
        self.assertEqual(self.main.comboBox.count(), 7)

    def test_checkbox_deselect(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/timings.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        QTest.mouseClick(self.main.paramsGrid.itemAt(0).widget(), Qt.LeftButton)
        self.assertEqual(self.main.paramsGrid.itemAt(0).widget().isChecked(), False)
        self.assertEqual(self.main.gridLayout.count(), 4)

    def test_checkbox_select(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/timings.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        QTest.mouseClick(self.main.paramsGrid.itemAt(0).widget(), Qt.LeftButton)
        self.assertEqual(self.main.paramsGrid.itemAt(0).widget().isChecked(), False)
        self.assertEqual(self.main.gridLayout.count(), 4)

        QTest.mouseClick(self.main.paramsGrid.itemAt(0).widget(), Qt.LeftButton)
        self.assertEqual(self.main.paramsGrid.itemAt(0).widget().isChecked(), True)
        self.assertEqual(self.main.gridLayout.count(), 5)

    def test_combobox_none(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/timings.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        self.main.comboBox.setCurrentIndex(self.main.comboBox.findText('NONE'))
        self.assertEqual(self.main.gridLayout.count(), 0)

    def test_combobox_all(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/timings.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        self.main.comboBox.setCurrentIndex(self.main.comboBox.findText('NONE'))
        self.assertEqual(self.main.gridLayout.count(), 0)

        self.main.comboBox.setCurrentIndex(self.main.comboBox.findText('ALL'))
        self.assertEqual(self.main.gridLayout.count(), 5)

    def test_combobox_one(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/timings.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        self.main.comboBox.setCurrentIndex(self.main.comboBox.findText('NONE'))
        self.assertEqual(self.main.gridLayout.count(), 0)

        self.main.comboBox.setCurrentIndex(self.main.comboBox.findText('MIN BOOST'))
        self.assertEqual(self.main.gridLayout.count(), 1)
        self.assertEqual(self.main.gridLayout.itemAt(0).itemAt(1).widget().figure.get_axes()[0].get_xlabel(), 'MIN BOOST')

    def test_correct_loaded_values(self):
        self.main = MainController.MainWindow()
        self.results_controller = MainController.MainResultsTabController(self.main)
        self.results_controller.initUiComponents()
        
        file = open('/home/seanc/Documents/Uni-Work/Year-4/Masters-Project/FinalUI/bin/correct_values.txt', 'r')
        file.seek(0)
        self.results_controller.loadResults(file)
        file.close()

        self.assertEqual(self.results_controller._paramValueMap['MIN BOOST'], ['200', '500', '1000'])
        self.assertEqual(self.results_controller._paramValueMap['MAX BOOST'], ['2500', '4000', '10000'])
        self.assertEqual(self.results_controller._paramValueMap['PERIOD (SECONDS)'], ['5', '7.5', '15'])
        self.assertEqual(self.results_controller._paramValueMap['SYNC WINDOW'], ['1000', '2000', '1000'])
        self.assertEqual(self.results_controller._paramValueMap['NUM DEVICES'], ['3', '3', '2'])
        self.assertEqual(self.results_controller._paramValueMap['RESULT'], ['141.8', '132.2', '176.1'])


if __name__ == '__main__':
    unittest.main()