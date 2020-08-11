#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:00:28 2020

@author: Lau
"""

import sys
from PyQt5 import QtWidgets, uic
import MolarMassCalculator_console as main
import numpy as np
import pandas as pd
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app = QtWidgets.QApplication(sys.argv)


#app.setStyle("Fusion")

window = uic.loadUi("mainwindow.ui")

def on_button_clicked():
    name = window.input_name.text()
    tmp_row_numb = window.dataframe.rowCount()
    if tmp_row_numb is not 0:
        for _ in range(tmp_row_numb):
	        window.dataframe.removeRow(0)
    if name != '':
        structure = main.molar_mass(name)
        M = structure()
        window.label_2.setText(f'The structure {name} has a molar mass of {M} g/mol.')
        number_elements = structure.data.shape[0]
        for i in range(number_elements):
            window.dataframe.insertRow(i)
            window.dataframe.setItem(i, 0, QtWidgets.QTableWidgetItem(structure.data.loc[i, "Element"]))
            window.dataframe.setItem(i, 1, QtWidgets.QTableWidgetItem(str(structure.data.loc[i][1])))
            window.dataframe.setItem(i, 2, QtWidgets.QTableWidgetItem(str(structure.data.loc[i, "Quantity"])))
            window.dataframe.setItem(i, 3, QtWidgets.QTableWidgetItem(str(structure.data.loc[i, "Total Molar Mass"])))
        return 0
    else:
        print('Please insert a chemical formular first!')
        window.label_2.setText(f'Please insert a chemical formular first!')
        window.calc_button.setDisabled(True)
        return 1

def show_about_dialog():
    text = "<center>" \
        "<h1>Molar Mass Calculator</h1>" \
        "</center>" \
        "<p>Version v1.0.0<br/>" \
        "Copyright &copy; 2020 Lau.</p>"\
        "Distributed under the terms of the General Public Licence V3."

    QMessageBox.about(window, "About Molar Mass Calculator", text)
def show_help_dialog():
    text = "<h1>Help: Molar Mass Calculator</h1>"\
        "<center>"\
        "Further information"
    QMessageBox.about(window, "Help", text)
def dark_mode():
    mode = 'dark'
    color_mode(mode)
    color_mode(mode)
def light_mode():
    mode = 'light'
    color_mode(mode)
    color_mode(mode)
def color_mode(mode):
    if mode == 'dark':
        color1 = QColor(53, 53, 53)
        color2 = Qt.white
        qss = """
        QMenuBar {
            background-color: QColor(50, 50, 50);
        }
        QMenuBar::item {
            spacing: 3px;
            padding: 2px 10px;
            background-color: QColor(53, 53, 53);
            color: Qt.white;
            border-radius: 5px;
        }
        QMenu {
            background-color: QColor(53, 53, 53);
            border: 1px solid black;
            margin: 2px;
        }
        QMenu::item {
            background-color: transparent;
        }
        """
    elif mode == 'light':
        color1 = Qt.white
        color2 = Qt.black
        qss = """
        QMenuBar {
            background-color: Qt.white;
        }
        QMenuBar::item {
            spacing: 3px;
            padding: 2px 10px;
            background-color: Qt.white;
            color: Qt.black;
            border-radius: 5px;
        }
        QMenu {
            background-color: Qt.white;
            border: 1px solid black;
            margin: 2px;
        }
        QMenu::item {
            background-color: transparent;
        }
        """
    else:
        print("color mode error")

    # -----     Set Palette:  ----- #
    palette = QPalette()
    palette.setColor(QPalette.Window, color1)
    palette.setColor(QPalette.Base, color1)
    palette.setColor(QPalette.Button, color1)
    palette.setColor(QPalette.WindowText, color2)
    palette.setColor(QPalette.Text, color2)
    palette.setColor(QPalette.ButtonText, color2)
    window.input_name.setPalette(palette)
    window.sample_mass.setPalette(palette)
    window.label_2.setPalette(palette)
    #window.tabWidget.setPalette(palette)
    #window.tabWidget.tabBar().setTabTextColor(0, color2)
    window.menubar.setStyleSheet(qss)
    #window.tabWidget.setStyleSheet(qss_tab)
    #app.setStyleSheet(qss_tab)
    #window.tabWidget.setStyleSheet("QWidget {background-color: yellow }")
    #more..
    app.setPalette(palette)
    # -----                 ----- #

def remRow():
    window.tableWidget.removeRow(window.tableWidget.rowCount()-1)
def addRow():
    window.tableWidget.insertRow(window.tableWidget.rowCount())
def mass_calc():
    name = window.input_name.text()
    if name != '':
        # Fails without warning if wrong name is given
        structure = main.molar_mass(name)
        M = structure()
    else:
        print('Please insert a sample mass first!')
        window.calc_mass.setDisabled(True)
        return 1
    sample_mass = window.sample_mass.text()
    try:
        sample_mass = float(sample_mass)
    except ValueError:
        raise
    number_reagents = window.tableWidget.rowCount()
    pre_input = pd.DataFrame(np.empty((number_reagents, 2)), columns=["Precursor", "Quantity"])
    for n in range(number_reagents):
        pre_input.loc[n, "Precursor"] = window.tableWidget.item(n, 0).text()
        pre_input.loc[n, "Quantity"] = window.tableWidget.item(n, 1).text()
    pre_data = structure.precursor(pre_input, sample_mass)
    for i in range(number_reagents):
        window.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(pre_data.loc[i, "Gram"])))
    return 0

def enable_calc_button():
    window.calc_button.setDisabled(False)
def enable_mass_button():
    window.calc_mass.setDisabled(False)
window.calc_button.setDisabled(True)
window.calc_mass.setDisabled(True)
window.input_name.textChanged.connect(enable_calc_button)
window.sample_mass.textChanged.connect(enable_mass_button)
window.addRow.clicked.connect(addRow)
window.delRow.clicked.connect(remRow)
window.calc_mass.clicked.connect(mass_calc)
window.calc_button.clicked.connect(on_button_clicked)
# Actions
window.actionAbout.triggered.connect(show_about_dialog)
window.actionHelp_Readme.triggered.connect(show_help_dialog)
window.actionDark_mode.triggered.connect(dark_mode)
window.actionLight_mode.triggered.connect(light_mode)
#window.exit_button.clicked.connect(app.exit)
window.show()
app.exec()
