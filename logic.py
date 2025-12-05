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
        self.submitButton.clicked.connect(self.submit)


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

    def submit(self):
        '''
        This Function is used to submit the candidate and id to a csv, unless the id boofs
        '''
        try:
            int(self.idLineEdit.text())
        except ValueError:
            self.idLabel.setText('ID must consist of numbers')
        else:
            if len(self.idLineEdit.text()) != 5:
                self.idLabel.setText('ID must be five (5) digits')
            else:
                with open('data.csv', 'w', newline='') as csvfile:
                    if self.idLineEdit.text() in csv.reader(csvfile):
                        self.idLabel.setText('ID has already voted')
                    else:
                        if self.janeRadioButton.isChecked():
                            vote = 'Jane Doe'
                        elif self.johnRadioButton.isChecked():
                            vote = 'John Doe'
                        elif self.otherRadioButton.isChecked():
                            print('wow')
                            # if len((self.otherLineEdit.text().strip())) != 2:
                            #     self.idLabel.setText('Your candidate must have a first and last name')
                            #     exit()

