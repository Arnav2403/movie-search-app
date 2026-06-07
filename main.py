import streamlit as st


PERIODIC_TABLE = {
    1: {"symbol": "H", "name": "Hydrogen", "atomic_mass": 1.008, "category": "Nonmetal", "group": 1, "period": 1, "electron_configuration": "1s1"},
    2: {"symbol": "He", "name": "Helium", "atomic_mass": 4.0026, "category": "Noble Gas", "group": 18, "period": 1, "electron_configuration": "1s2"},
    3: {"symbol": "Li", "name": "Lithium", "atomic_mass": 6.94, "category": "Alkali Metal", "group": 1, "period": 2, "electron_configuration": "1s2 2s1"},
    4: {"symbol": "Be", "name": "Beryllium", "atomic_mass": 9.0122, "category": "Alkaline Earth Metal", "group": 2, "period": 2, "electron_configuration": "1s2 2s2"},
    5: {"symbol": "B", "name": "Boron", "atomic_mass": 10.81, "category": "Metalloid", "group": 13, "period": 2, "electron_configuration": "1s2 2s2 2p1"},
    6: {"symbol": "C", "name": "Carbon", "atomic_mass": 12.011, "category": "Nonmetal", "group": 14, "period": 2, "electron_configuration": "1s2 2s2 2p2"},
    7: {"symbol": "N", "name": "Nitrogen", "atomic_mass": 14.007, "category": "Nonmetal", "group": 15, "period": 2, "electron_configuration": "1s2 2s2 2p3"},
    8: {"symbol": "O", "name": "Oxygen", "atomic_mass": 15.999, "category": "Nonmetal", "group": 16, "period": 2, "electron_configuration": "1s2 2s2 2p4"},
    9: {"symbol": "F", "name": "Fluorine", "atomic_mass": 18.998, "category": "Halogen", "group": 17, "period": 2, "electron_configuration": "1s2 2s2 2p5"},
    10: {"symbol": "Ne", "name": "Neon", "atomic_mass": 20.180, "category": "Noble Gas", "group": 18, "period": 2, "electron_configuration": "1s2 2s2 2p6"},
    11: {"symbol": "Na", "name": "Sodium", "atomic_mass": 22.990, "category": "Alkali Metal", "group": 1, "period": 3, "electron_configuration": "1s2 2s2 2p6 3s1"},
    12: {"symbol": "Mg", "name": "Magnesium", "atomic_mass": 24.305, "category": "Alkaline Earth Metal", "group": 2, "period": 3, "electron_configuration": "1s2 2s2 2p6 3s2"},
    13: {"symbol": "Al", "name": "Aluminum", "atomic_mass": 26.982, "category": "Post-transition Metal", "group": 13, "period": 3, "electron_configuration": "1s2 2s2 2p6 3s2 3p1"},
    14: {"symbol": "Si", "name": "Silicon", "atomic_mass": 28.085, "category": "Metalloid", "group": 14, "period": 3, "electron_configuration": "1s2 2s2 2p6 3s2 3p2"},
    15: {"symbol": "P", "name": "Phosphorus", "atomic_mass": 30.974, "category": "Nonmetal", "group": 15, "period": 3, "electron_configuration": "1s2 2s2 2p6 3s2 3p3"},
    16: {"symbol": "S", "name": "Sulfur", "atomic_mass": 32.06, "category": "Nonmetal", "group": 16, "period": 3, "electron_configuration": "1s2 2s2 2p6 3s2 3p4"},
    17: {"symbol": "Cl", "name": "Chlorine", "atomic_mass": 35.45, "category": "Halogen", "group": 17, "period": 3, "electron_configuration": "1s2 2s2 2p6 3s2 3p5"},
    18: {"symbol": "Ar", "name": "Argon", "atomic_mass": 39.948, "category": "Noble Gas", "group": 18, "period": 3, "electron_configuration": "1s2 2s2 2p6 3s2 3p6"},
    19: {"symbol": "K", "name": "Potassium", "atomic_mass": 39.098, "category": "Alkali Metal", "group": 1, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s1"},
    20: {"symbol": "Ca", "name": "Calcium", "atomic_mass": 40.078, "category": "Alkaline Earth Metal", "group": 2, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2"},
    21: {"symbol": "Sc", "name": "Scandium", "atomic_mass": 44.956, "category": "Transition Metal", "group": 3, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 3d1 4s2"},
    22: {"symbol": "Ti", "name": "Titanium", "atomic_mass": 47.867, "category": "Transition Metal", "group": 4, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 3d2 4s2"},
    23: {"symbol": "V", "name": "Vanadium", "atomic_mass": 50.942, "category": "Transition Metal", "group": 5, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 3d3 4s2"},
    24: {"symbol": "Cr", "name": "Chromium", "atomic_mass": 52.00, "category": "Transition Metal", "group": 6, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 3d5 4s1"},
    25: {"symbol": "Mn", "name": "Manganese", "atomic_mass": 54.938, "category": "Transition Metal", "group": 7, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 3d5 4s2"},
    26: {"symbol": "Fe", "name": "Iron", "atomic_mass": 55.845, "category": "Transition Metal", "group": 8, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 3d6 4s2"},
    27: {"symbol": "Co", "name": "Cobalt", "atomic_mass": 58.933, "category": "Transition Metal", "group": 9, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 3d7 4s2"},
    28: {"symbol": "Ni", "name": "Nickel", "atomic_mass": 58.693, "category": "Transition Metal", "group": 10, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 3d8 4s2"},
    29: {"symbol": "Cu", "name": "Copper", "atomic_mass": 63.546, "category": "Transition Metal", "group": 11, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 3d10 4s1"},
    30: {"symbol": "Zn", "name": "Zinc", "atomic_mass": 65.38, "category": "Transition Metal", "group": 12, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 3d10 4s2"},
    31: {"symbol": "Ga", "name": "Gallium", "atomic_mass": 69.723, "category": "Post-transition Metal", "group": 13, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p1"},
    32: {"symbol": "Ge", "name": "Germanium", "atomic_mass": 72.63, "category": "Metalloid", "group": 14, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p2"},
    33: {"symbol": "As", "name": "Arsenic", "atomic_mass": 74.922, "category": "Metalloid", "group": 15, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p3"},
    34: {"symbol": "Se", "name": "Selenium", "atomic_mass": 78.971, "category": "Nonmetal", "group": 16, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p4"},
    35: {"symbol": "Br", "name": "Bromine", "atomic_mass": 79.904, "category": "Halogen", "group": 17, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p5"},
    36: {"symbol": "Kr", "name": "Krypton", "atomic_mass": 83.798, "category": "Noble Gas", "group": 18, "period": 4, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6"},
    37: {"symbol": "Rb", "name": "Rubidium", "atomic_mass": 85.468, "category": "Alkali Metal", "group": 1, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s1"},
    38: {"symbol": "Sr", "name": "Strontium", "atomic_mass": 87.62, "category": "Alkaline Earth Metal", "group": 2, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2"},
    39: {"symbol": "Y", "name": "Yttrium", "atomic_mass": 88.905, "category": "Transition Metal", "group": 3, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d1 5s2"},
    40: {"symbol": "Zr", "name": "Zirconium", "atomic_mass": 91.224, "category": "Transition Metal", "group": 4, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d2 5s2"},
    41: {"symbol": "Nb", "name": "Niobium", "atomic_mass": 92.906, "category": "Transition Metal", "group": 5, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d4 5s1"},
    42: {"symbol": "Mo", "name": "Molybdenum", "atomic_mass": 95.95, "category": "Transition Metal", "group": 6, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d5 5s1"},
    43: {"symbol": "Tc", "name": "Technetium", "atomic_mass": 98.0, "category": "Transition Metal", "group": 7, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d5 5s2"},
    44: {"symbol": "Ru", "name": "Ruthenium", "atomic_mass": 101.07, "category": "Transition Metal", "group": 8, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d7 5s1"},
    45: {"symbol": "Rh", "name": "Rhodium", "atomic_mass": 102.91, "category": "Transition Metal", "group": 9, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d8 5s1"},
    46: {"symbol": "Pd", "name": "Palladium", "atomic_mass": 106.42, "category": "Transition Metal", "group": 10, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10"},
    47: {"symbol": "Ag", "name": "Silver", "atomic_mass": 107.868, "category": "Transition Metal", "group": 11, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s1"},
    48: {"symbol": "Cd", "name": "Cadmium", "atomic_mass": 112.41, "category": "Transition Metal", "group": 12, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2"},
    49: {"symbol": "In", "name": "Indium", "atomic_mass": 114.82, "category": "Post-transition Metal", "group": 13, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p1"},
    50: {"symbol": "Sn", "name": "Tin", "atomic_mass": 118.71, "category": "Post-transition Metal", "group": 14, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p2"},
    51: {"symbol": "Sb", "name": "Antimony", "atomic_mass": 121.76, "category": "Metalloid", "group": 15, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p3"},
    52: {"symbol": "Te", "name": "Tellurium", "atomic_mass": 127.60, "category": "Metalloid", "group": 16, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p4"},
    53: {"symbol": "I", "name": "Iodine", "atomic_mass": 126.90, "category": "Halogen", "group": 17, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p5"},
    54: {"symbol": "Xe", "name": "Xenon", "atomic_mass": 131.29, "category": "Noble Gas", "group": 18, "period": 5, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 5s2 5p6"},
    55: {"symbol": "Cs", "name": "Cesium", "atomic_mass": 132.91, "category": "Alkali Metal", "group": 1, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s1"},
    56: {"symbol": "Ba", "name": "Barium", "atomic_mass": 137.33, "category": "Alkaline Earth Metal", "group": 2, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2"},
    57: {"symbol": "La", "name": "Lanthanum", "atomic_mass": 138.91, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d1 6s2"},
    58: {"symbol": "Ce", "name": "Cerium", "atomic_mass": 140.12, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d1 5s2"},
        58: {"symbol": "Ce", "name": "Cerium", "atomic_mass": 140.12, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d1 5s2"},
    59: {"symbol": "Pr", "name": "Praseodymium", "atomic_mass": 140.91, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d2 5s2"},
    60: {"symbol": "Nd", "name": "Neodymium", "atomic_mass": 144.24, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d3 5s2"},
    61: {"symbol": "Pm", "name": "Promethium", "atomic_mass": 145.0, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d4 5s2"},
    62: {"symbol": "Sm", "name": "Samarium", "atomic_mass": 150.36, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d5 5s2"},
    63: {"symbol": "Eu", "name": "Europium", "atomic_mass": 151.98, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d6 5s2"},
    64: {"symbol": "Gd", "name": "Gadolinium", "atomic_mass": 157.25, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d7 5s2"},
    65: {"symbol": "Tb", "name": "Terbium", "atomic_mass": 158.93, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d8 5s2"},
    66: {"symbol": "Dy", "name": "Dysprosium", "atomic_mass": 162.50, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d9 5s2"},
    67: {"symbol": "Ho", "name": "Holmium", "atomic_mass": 164.93, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    68: {"symbol": "Er", "name": "Erbium", "atomic_mass": 167.26, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    69: {"symbol": "Tm", "name": "Thulium", "atomic_mass": 168.93, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    70: {"symbol": "Yb", "name": "Ytterbium", "atomic_mass": 173.04, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    71: {"symbol": "Lu", "name": "Lutetium", "atomic_mass": 175.0, "category": "Lanthanide", "group": 3, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    72: {"symbol": "Hf", "name": "Hafnium", "atomic_mass": 178.49, "category": "Transition Metal", "group": 4, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    73: {"symbol": "Ta", "name": "Tantalum", "atomic_mass": 180.95, "category": "Transition Metal", "group": 5, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    74: {"symbol": "W", "name": "Tungsten", "atomic_mass": 183.84, "category": "Transition Metal", "group": 6, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    75: {"symbol": "Re", "name": "Rhenium", "atomic_mass": 186.21, "category": "Transition Metal", "group": 7, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    76: {"symbol": "Os", "name": "Osmium", "atomic_mass": 190.23, "category": "Transition Metal", "group": 8, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    77: {"symbol": "Ir", "name": "Iridium", "atomic_mass": 192.22, "category": "Transition Metal", "group": 9, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    78: {"symbol": "Pt", "name": "Platinum", "atomic_mass": 195.08, "category": "Transition Metal", "group": 10, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    79: {"symbol": "Au", "name": "Gold", "atomic_mass": 196.97, "category": "Transition Metal", "group": 11, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    80: {"symbol": "Hg", "name": "Mercury", "atomic_mass": 200.59, "category": "Transition Metal", "group": 12, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    81: {"symbol": "Tl", "name": "Thallium", "atomic_mass": 204.38, "category": "Post-transition Metal", "group": 13, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    82: {"symbol": "Pb", "name": "Lead", "atomic_mass": 207.2, "category": "Post-transition Metal", "group": 14, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    83: {"symbol": "Bi", "name": "Bismuth", "atomic_mass": 208.98, "category": "Post-transition Metal", "group": 15, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    84: {"symbol": "Po", "name": "Polonium", "atomic_mass": 209.98, "category": "Metalloid", "group": 16, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    85: {"symbol": "At", "name": "Astatine", "atomic_mass": 210.0, "category": "Metalloid", "group": 17, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    86: {"symbol": "Rn", "name": "Radon", "atomic_mass": 222.0, "category": "Noble Gas", "group": 18, "period": 6, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    87: {"symbol": "Fr", "name": "Francium", "atomic_mass": 223.0, "category": "Alkali Metal", "group": 1, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 7s1"},
    88: {"symbol": "Ra", "name": "Radium", "atomic_mass": 226.03, "category": "Alkaline Earth Metal", "group": 2, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 7s2"},
    89: {"symbol": "Ac", "name": "Actinium", "atomic_mass": 227.0, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f1 7s2"},
    90: {"symbol": "Th", "name": "Thorium", "atomic_mass": 232.04, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f2 7s2"},
    91: {"symbol": "Pa", "name": "Protactinium", "atomic_mass": 231.04, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f3 7s2"},
    92: {"symbol": "U", "name": "Uranium", "atomic_mass": 238.03, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f4 7s2"},
    93: {"symbol": "Np", "name": "Neptunium", "atomic_mass": 237.0, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f5 7s2"},
    94: {"symbol": "Pu", "name": "Plutonium", "atomic_mass": 244.0, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f6 7s2"},
    95: {"symbol": "Am", "name": "Americium", "atomic_mass": 243.0, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f7 7s2"},
    96: {"symbol": "Cm", "name": "Curium", "atomic_mass": 247.0, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f8 7s2"},
    97: {"symbol": "Bk", "name": "Berkelium", "atomic_mass": 247.0, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f9 7s2"},
    98: {"symbol": "Cf", "name": "Californium", "atomic_mass": 251.0, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f10 7s2"},
    99: {"symbol": "Es", "name": "Einsteinium", "atomic_mass": 252.0, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f11 7s2"},
    100: {"symbol": "Fm", "name": "Fermium", "atomic_mass": 257.0, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f12 7s2"},
    101: {"symbol": "Md", "name": "Mendelevium", "atomic_mass": 258.0, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f13 7s2"},
    102: {"symbol": "No", "name": "Nobelium", "atomic_mass": 259.0, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f14 7s2"},
    103: {"symbol": "Lr", "name": "Lawrencium", "atomic_mass": 262.0, "category": "Actinide", "group": 3, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 6s2 5f14 7s2"},
    104: {"symbol": "Rf", "name": "Rutherfordium", "atomic_mass": 267.0, "category": "Transition Metal", "group": 4, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    105: {"symbol": "Db", "name": "Dubnium", "atomic_mass": 270.0, "category": "Transition Metal", "group": 5, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    106: {"symbol": "Sg", "name": "Seaborgium", "atomic_mass": 271.0, "category": "Transition Metal", "group": 6, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    107: {"symbol": "Bh", "name": "Bohrium", "atomic_mass": 270.0, "category": "Transition Metal", "group": 7, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    108: {"symbol": "Hs", "name": "Hassium", "atomic_mass": 277.0, "category": "Transition Metal", "group": 8, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    109: {"symbol": "Mt", "name": "Meitnerium", "atomic_mass": 278.0, "category": "Transition Metal", "group": 9, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    110: {"symbol": "Ds", "name": "Darmstadtium", "atomic_mass": 281.0, "category": "Transition Metal", "group": 10, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    111: {"symbol": "Rg", "name": "Roentgenium", "atomic_mass": 280.0, "category": "Transition Metal", "group": 11, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    112: {"symbol": "Cn", "name": "Copernicium", "atomic_mass": 285.0, "category": "Transition Metal", "group": 12, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    113: {"symbol": "Nh", "name": "Nihonium", "atomic_mass": 284.0, "category": "Post-transition Metal", "group": 13, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    114: {"symbol": "Fl", "name": "Flerovium", "atomic_mass": 289.0, "category": "Post-transition Metal", "group": 14, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    115: {"symbol": "Mc", "name": "Moscovium", "atomic_mass": 288.0, "category": "Post-transition Metal", "group": 15, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    116: {"symbol": "Lv", "name": "Livermorium", "atomic_mass": 293.0, "category": "Post-transition Metal", "group": 16, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    117: {"symbol": "Ts", "name": "Tennessine", "atomic_mass": 294.0, "category": "Metalloid", "group": 17, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"},
    118: {"symbol": "Og", "name": "Oganesson", "atomic_mass": 294.0, "category": "Noble Gas", "group": 18, "period": 7, "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5p6 4d10 5s2"}
}


def add_gradient_text(text):
    return f'<h2 style="background: linear-gradient(90deg, #FF5733, #FFC300, #33FF57); -webkit-background-clip: text; color: transparent;">{text}</h2>'

def main():
    st.set_page_config(page_title="Periodic Table Explorer", layout="centered")
    st.title("🧪 Periodic Table Explorer")
    st.caption("Discover details of elements by name, symbol, or atomic number.")

    with st.sidebar:
        st.header("🔍 Search Options")
        search_mode = st.radio("Search by:", ["Name", "Symbol", "Atomic Number"])

    if search_mode == "Name":
        names = [data["name"] for data in PERIODIC_TABLE.values()]
        selected = st.selectbox("Choose an element by name:", sorted(names))
        result = next((el for el in PERIODIC_TABLE.values() if el["name"] == selected), None)
    elif search_mode == "Symbol":
        symbols = [data["symbol"] for data in PERIODIC_TABLE.values()]
        selected = st.selectbox("Choose an element by symbol:", sorted(symbols))
        result = next((el for el in PERIODIC_TABLE.values() if el["symbol"] == selected), None)
    else:  # Atomic Number
        atomic_numbers = sorted(PERIODIC_TABLE.keys())
        selected = st.selectbox("Choose an atomic number:", atomic_numbers)
        result = PERIODIC_TABLE.get(selected)

    if result:
        st.markdown("---")
        st.subheader(f"🧬 Element Details: {result.get('name')}")

        col1, col2 = st.columns([2, 1])
        with col1:
            for key, value in result.items():
                if key not in ["image_url", "trivia"]:
                    st.markdown(f"**{key}:** {value}")
        with col2:
            if "image_url" in result:
                st.image(result["image_url"], caption=f"{result.get('name')} image", use_column_width=True)
    else:
        st.error("Element not found.")

if __name__ == "__main__":
    main()
