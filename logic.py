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
        foundID = False
        voted = True
        try:
            int(self.idLineEdit.text())
        except ValueError:
            self.idLabel.setText('ID must consist of numbers')
        else:
            if len(self.idLineEdit.text()) != 5:
                self.idLabel.setText('ID must be five (5) digits')
            else:
                try:
                    csvTestFile = open('data.csv', 'r')
                    csvTestFile.close()
                except FileNotFoundError:
                    csvCreateFile = open('data.csv', 'w', newline='')
                    csv.writer(csvCreateFile).writerow(['Candidate', 'ID Number'])
                    csvCreateFile.close()

                with open('data.csv', 'r', newline='') as csvfile:
                    for row in csv.reader(csvfile):
                        if self.idLineEdit.text() in row:
                            self.idLabel.setText('ID has already voted')
                            foundID = True
                        else:
                            numberID = self.idLineEdit.text()
                    if self.janeRadioButton.isChecked():
                        vote = 'Jane Doe'
                    elif self.johnRadioButton.isChecked():
                        vote = 'John Doe'
                    elif self.otherRadioButton.isChecked():
                        vote = self.otherLineEdit.text()
                    else:
                        voted = False

                if not foundID and voted:
                    with open('data.csv', 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([vote, numberID])
                        self.resetEntries()
                elif not voted:
                    self.idLabel.setText('Must select a candidate')

    def resetEntries(self):
        '''
        This Function is used to clear the entries entered by the user and set all text back to original.
        Will also unfocus the user if they are still on the textbox
        '''
        self.idLabel.setText('Please enter an ID number (5 digits)')
        self.otherLineEdit.setText('')
        if self.buttonGroup.checkedButton() != None:
            self.buttonGroup.setExclusive(False)
            self.buttonGroup.checkedButton().setChecked(False)
            self.buttonGroup.setExclusive(True)
        self.idLineEdit.setText('')



