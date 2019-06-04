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
folder = 'C:/Users/z5119993/OneDrive - UNSW/research/measurements/ICE He3/BA11' #for Windows
file = 'BA11_PBG_500mK_n10_V14.05.csv'


file_csv = folder + '/' + file


file_txt = file_csv.replace('csv', 'txt')

ut.convertCSVtoTXT(file_csv, file_txt)

# Using library "resonator_tools" for fitting notch type resonators
port1 = circuit.reflection_port()

port1.add_fromtxt(file_txt, 'dBmagphasedeg', 1, delimiter=' ')
print('reading of the data is successfully finished')
#port1.add_fromtxt(file_csv,'linmagphasedeg',3)


port1.autofit(electric_delay=None)
print('autofit is done')
print("Fit results:", port1.fitresults)
port1.plotall()

port1.GUIfit()

print("single photon limit:",
      port1.get_single_photon_limit(diacorr=True), "dBm")
# print("photons in reso for input -140dBm:",
#       port1.get_photons_in_resonator(-140, unit='dBm', diacorr=True),
#       "photons")

