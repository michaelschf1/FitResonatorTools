'''
Created on 1 Oct. 2018

@author: Mykhailo Savytskyi

@email: m.savytskyi@unsw.edu.au
'''

from resonator_tools import circuit

import FitResonatorTools.src.utilities as ut
import pandas as pd

# Data file path
#folder  = '/Users/mykhailo/OneDrive - UNSW/research/measurements/ICE He3/BA11' #for Mac
folder = 'C:/Users/z5119993/OneDrive - UNSW/research/measurements/ICE He3/A9nm_CA1' #for Windows
file = 'CA1_LGR_RT_N15_7_COM.csv'


file_csv = folder + '/' + file


file_txt = file_csv.replace('csv', 'txt')

ut.convertCSVtoTXT(file_csv, file_txt)

# Using library "resonator_tools" for fitting notch type resonators
port1 = circuit.reflection_port()

port1.add_fromtxt(file_txt, 'dBmagphasedeg', 18, delimiter=' ')
print('reading of the data is successfully finished')
#port1.add_fromtxt(file_csv,'linmagphasedeg',3)


# port1.autofit(electric_delay=None)
# # port1.GUIbaselinefit()
# print('autofit is done')
# print("Fit results:", port1.fitresults)
# port1.GUIbaselinefit()

# fit the corrected data
port1.GUIfit()
print("Fit results:", port1.fitresults)
port1.plotall()

# print("single photon limit:",
#       port1.get_single_photon_limit(diacorr=True), "dBm")
# print("photons in reso for input -140dBm:",
#       port1.get_photons_in_resonator(-140, unit='dBm', diacorr=True),
#       "photons")

