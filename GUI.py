# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:00:28 2020

@author: Lau
"""

import sys
from PyQt5 import QtWidgets, uic
import MolarMassCalculator as main
import numpy as np
import pandas as pd

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("mainwindow.ui")

window.label.setText(f'Welcome to Version v{main.VERSION}')

def on_button_clicked():
    name = window.input_name.text()
    if name is not '':
        structure = main.molar_mass(name)
        M = structure()
        window.label_2.setText(f'The structure {name} has a molar mass of {M} g/mol.')
        return 0
    else:
        print('Please insert a chemical formular first!')
        window.label_2.setText(f'Please insert a chemical formular first!')
        return 1
def about():
    window_about = uic.loadUi("about.ui")
    window_about.show()
def remRow():
    window.tableWidget.removeRow(1)
def addRow():
    window.tableWidget.insertRow(1)
def mass_calc():
    name = window.input_name_2.text()
    if name is not '':
        structure = main.molar_mass(name)
        M = structure()
    else:
        print('Please insert a chemical formular first!')
        window.label_2.setText(f'Please insert a chemical formular first!')
        return 1
    print(M)
    sample_mass = window.sample_mass.text()
    try:
        sample_mass = float(sample_mass)
    except ValueError:
        raise
    number_reagents = window.tableWidget.rowCount()
    pre_input = pd.DataFrame(np.empty((number_reagents, 2)), columns=[
                    "Precursor", "Quantity"])
    for n in range(number_reagents):
        pre_input.loc[n, "Precursor"] = window.tableWidget.item(0,0).text()
        pre_input.loc[n, "Quantity"] = window.tableWidget.item(0,1).text()
    print(pre_input)
    #structure.precursor()

    return 0
window.calc_button.clicked.connect(on_button_clicked)
window.actionAbout.triggered.connect(about)
window.addRow.clicked.connect(addRow)
window.delRow.clicked.connect(remRow)
window.calc_mass.clicked.connect(mass_calc)
#window.exit_button.clicked.connect(app.exit)
window.show()
app.exec()
