[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub issues](https://img.shields.io/github/issues/LauKr/Molar-mass-calculator)](https://GitHub.com/LauKr/Molar-mass-calculator/issues/) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE) ![GitHub commits since tagged version](https://img.shields.io/github/commits-since/LauKr/Molar-mass-calculator/v0.1) ![GitHub repo size](https://img.shields.io/github/repo-size/LauKr/Molar-mass-calculator) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3957938.svg)](https://doi.org/10.5281/zenodo.3957938) 

# Molar mass calculator
 A simple calculator for molar masses of compounds.

## Getting Started

### Prerequisites

The program requires Python 3.x
```
$ apt-get install python3.6
```
as well as numpy, pandas & PyQt5 (for GUI only)
```
$ pip install numpy pandas PyQt5
```

### Setup

Get the .py file by either cloning, downloading or downloading as .zip and unzipping.
Then use python for starting the [MolarMassCalculator_console.py](MolarMassCalculator_console.py) file.

For example:
```
$ python3 Molar-mass-calculator/MolarMassCalculator_console.py
```

### Usage

Either use the GUI.py for a graphical interface or use MolarMassCalculator_console.py for a console input based version.

#### Basics
The program should ask for a structure name. This name can be inserted like _La2O3_. If the name cannot automatically converted into the necessary information which elements occure how often, the user will be asked to insert this information manually.
The molar mass is is printed and the user will be asked if he/she wants to calculate the precursor masses necessary for the reaction.
This information should be inserted like in the following example:

**Reaction:** H2 + 1/2 O2 -> H2O

Console only:

**Input:**

_How many precursors do you use?_ **2**

_What is precursor No. 1 called?_ **H2**

_How often is the precursor present?_ **1**

_What is precursor No. 1 called?_ **O2**

_How often is the precursor present?_ **0.5**

_How much sample do you want to synthesize? [g]_ **1**

**Output:**

You will need 0.1119 g of H2

You will need 0.8881 g of O2


#### Advanced

The program has a class molar_mass(), which takes the optinal argument <name>. If <name> is given this will be treated as the structre, if not the program will aks for it.
You can use
 ```
 sample123 = molar_mass("H2O")
 print(sample123)
 ```
 to get the information on the molar mass, or just 
 ```
 M = calculate("H2O")
 ```
 to initialize M with the molar mass as a float.
 
 To calculate the precursor masses, you'll need to call
 ```
 sample123.precursor()
 ```
 
 If you want to access the data on the molar masses, you can use
 ```
 sample123.data
 sample123.precursor_data
 sample123.M
 ```
 for the data on the compound respectively the precursors and the total molar mass of the compound.

## Authors

* **Laurenz Kruty** - *Initial work* - [LauKr](https://github.com/LauKr)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgement

This project was created using not only [Python](https://www.python.org/), but also [Qt](https://www.qt.io/).
