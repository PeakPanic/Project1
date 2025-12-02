from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_VotingSheet):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.toggleOtherTextBox()
        self.janeRadioButton.clicked.connect(self.toggleOtherTextBox)
        self.johnRadioButton.clicked.connect(self.toggleOtherTextBox)
        self.otherRadioButton.clicked.connect(self.toggleOtherTextBox)


    def toggleOtherTextBox(self):
        '''
        This Function is used to toggle the text box for the other option and clears it depending on which radio button is checked
        '''
        if self.janeRadioButton.isChecked():
            self.otherLineEdit.setVisible(False)
            self.otherLineEdit.setText('')
        elif self.johnRadioButton.isChecked():
            self.otherLineEdit.setVisible(False)
            self.otherLineEdit.setText('')
        elif self.otherRadioButton.isChecked():
            self.otherLineEdit.setVisible(True)
        else:
            self.otherLineEdit.setVisible(False)
            self.otherLineEdit.setText('')