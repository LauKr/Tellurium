# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:31:32 2020

@author: Laurenz Kruty
"""

import numpy as np
import pandas as pd


Version = "0.1"

class MolarMass():
    def __init__(self):
        self.database = {
                        'H': 1.00794, 'He': 4.002602, 'Li': 6.941, 
                        'Be': 9.012182, 'B': 10.811, 'C': 12.0107, 
                        'N': 14.0067, 'O': 15.9994, 'F': 18.9984032,
                        'Ne': 20.1797, 'Na': 22.98976928, 'Mg': 24.305,
                        'Al': 26.9815386, 'Si': 28.0855, 'P': 30.973762,
                        'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.0983,
                        'Ca': 40.078, 'Sc': 44.955912, 'Ti': 47.867,
                        'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938045,
                        'Fe': 55.845, 'Co': 58.933195, 'Ni': 58.6934,
                        'Cu': 63.546, 'Zn': 65.409, 'Ga': 69.723, 'Ge': 72.64,
                        'As': 74.9216, 'Se': 78.96, 'Br': 79.904,
                        'Kr': 83.798, 'Rb': 85.4678, 'Sr': 87.62,
                        'Y': 88.90585, 'Zr': 91.224, 'Nb': 92.90638,
                        'Mo': 95.94, 'Tc': 98.9063, 'Ru': 101.07,
                        'Rh': 102.9055, 'Pd': 106.42, 'Ag': 107.8682,
                        'Cd': 112.411, 'In': 114.818, 'Sn': 118.71,
                        'Sb': 121.760, 'Te': 127.6, 'I': 126.90447,
                        'Xe': 131.293, 'Cs': 132.9054519, 'Ba': 137.327,
                        'La': 138.90547, 'Ce': 140.116, 'Pr': 140.90465,
                        'Nd': 144.242, 'Pm': 146.9151, 'Sm': 150.36,
                        'Eu': 151.964, 'Gd': 157.25, 'Tb': 158.92535,
                        'Dy': 162.5, 'Ho': 164.93032, 'Er': 167.259,
                        'Tm': 168.93421, 'Yb': 173.04, 'Lu': 174.967,
                        'Hf': 178.49, 'Ta': 180.9479, 'W': 183.84,
                        'Re': 186.207, 'Os': 190.23, 'Ir': 192.217,
                        'Pt': 195.084, 'Au': 196.966569, 'Hg': 200.59,
                        'Tl': 204.3833, 'Pb': 207.2, 'Bi': 208.9804,
                        'Po': 208.9824, 'At': 209.9871, 'Rn': 222.0176,
                        'Fr': 223.0197, 'Ra': 226.0254, 'Ac': 227.0278,
                        'Th': 232.03806, 'Pa': 231.03588, 'U': 238.02891,
                        'Np': 237.0482, 'Pu': 244.0642, 'Am': 243.0614,
                        'Cm': 247.0703, 'Bk': 247.0703, 'Cf': 251.0796,
                        'Es': 252.0829, 'Fm': 257.0951, 'Md': 258.0951,
                        'No': 259.1009, 'Lr': 262, 'Rf': 267, 'Db': 268,
                        'Sg': 271, 'Bh': 270, 'Hs': 269, 'Mt': 278, 'Ds': 281,
                        'Rg': 281, 'Cn': 285, 'Nh': 284, 'Fl': 289, 'Mc': 289,
                        'Lv': 292, 'Ts': 294, 'Og': 294
                        }
        self.hello()
    
    def hello(self):
        print(f'Hello, welcome to MolarMassCalculator Version {Version}.')
        print('')
        n = int(input('How many elements do you want to use?'))
        self.calculate(n)

    def calculate(self, n=1):
        self.data = pd.DataFrame(np.empty((n, 4)), columns = ["Element", "Molar Mass", "Quantity", "Total Molar Mass"])
        print('Now step by step:')
        for i in range(n):
            self.data.loc[i,"Element"] = input(f'What element is present?')
            self.data.loc[i,"Molar Mass"] = float(self.database[self.data.loc[i,"Element"]])
            self.data.loc[i,"Quantity"] = float(input('How often?'))
            self.data.loc[i,"Total Molar Mass"] = self.data.loc[i,"Molar Mass"] * self.data.loc[i,"Quantity"]
            self.M = self.data["Total Molar Mass"].sum()
        return self.M
    
    def __call__(self):
        """ If called, i.e. XYZ = MolarMass(); XYZ(), the functions returns the total Molar Mass."""
        return self.M

    def __repr__(self):
        structure = []
        for i in range(self.data["Element"].shape[0]):
            if self.data.loc[i,"Quantity"] == 1:
                structure.append(self.data.loc[i,"Element"])
            else:
                structure.append(self.data.loc[i,"Element"] + str(self.data.loc[i,"Quantity"]))
        structure = ''.join(structure)
        return f"The structure {structure} has a molar weigth of M={self.M} g/mol."
    
    def get_precursor(self):
        pre_number = int(input('How many precursors do you use?'))
        self.precursor_data = pd.DataFrame(np.empty((pre_number, 5)), columns = ["Precursor", "Molar Mass", "Quantity", "Total Molar Mass", "Gram"])
        print(f'Now for each precursor:')
        for i in range(pre_number):
            pre_name = input(f'What is precursor No. {i+1} called?')
            pre_m = int(input(f'How many elements does precursor No {i+1} ({pre_name}) have?'))
            precursor = pd.DataFrame(np.empty((pre_m, 4)), columns = ["Element", "Molar Mass", "Quantity", "Total Molar Mass"])
            for m in range(pre_m):
                precursor.loc[m,"Element"] = input(f'What element is present?')
                precursor.loc[m,"Molar Mass"] = float(self.database[precursor.loc[m,"Element"]])
                precursor.loc[m,"Quantity"] = float(input('How often?'))
                precursor.loc[m,"Total Molar Mass"] = precursor.loc[m,"Molar Mass"] * precursor.loc[m,"Quantity"]
            precursor_M = precursor["Total Molar Mass"].sum()
            self.precursor_data.loc[i, "Precursor"] = pre_name
            self.precursor_data.loc[i, "Molar Mass"] = precursor_M
            self.precursor_data.loc[i, "Quantity"] = float(input('How often is the precursor present?'))
            self.precursor_data.loc[i, "Total Molar Mass"] = self.precursor_data.loc[i,"Molar Mass"] * self.precursor_data.loc[i,"Quantity"]
        return self.precursor_data
    
    def precursor(self):
        print(f'Ah, you want to calculate the necessary precursor masses? Nice!')
        print(f"Let's try it!")
        self.get_precursor()
        sample_mass = float(input("How much sample do you want to synthesize? [g]"))
        sample_mol = sample_mass/self.M
        for i in range(self.precursor_data.shape[0]):
            self.precursor_data.loc[i, "Gram"] = self.precursor_data.loc[i, "Total Molar Mass"] * sample_mol
            print(f'You will need {round(self.precursor_data.loc[i, "Gram"],4)} g of {self.precursor_data.loc[i, "Precursor"]}')
        print(self.precursor_data)
        
        


if __name__ == "__main__":
    test = MolarMass()
    print(test)
    print(test.precursor())
