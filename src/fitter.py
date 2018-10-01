'''
Created on 1 Oct. 2018

@author: Mykhailo Savytskyi

@email: m.savytskyi@unsw.edu.au
'''

from resonator_tools import circuit
import numpy as np
import pandas as pd
from utilities import writeTXT, readCSV, trim


folder = '/Users/mykhailo/OneDrive - UNSW/research/measurements/Sample PBG AA1/LGR_PBG_28Aug18_1.4K_meas_NoCal/'
file_s21 = folder + 'SMA1-3_peak7.8_noDC_n20.csv'

fmin = 7.83  # frequency in [GHz]
fmax = 7.88 # frequency in [GHz]

data = readCSV(file_s21, headers=7)
data = trim(data, fmin, fmax)
writeTXT('S21.txt', data)

port1 = circuit.notch_port()
port1.add_fromtxt('S21.txt', 'dBmagphasedeg', 1)
print('reading of the data is succesfully finished')

# port1.autofit()
# print('autofit is done')
# print("Fit results:", port1.fitresults)
# port1.plotall()

port1.GUIfit()
print("Fit results:", port1.fitresults)
port1.plotall()
print("single photon limit:", port1.get_single_photon_limit(diacorr=True), "dBm")
print("photons in reso for input -140dBm:", port1.get_photons_in_resonator(-140,unit='dBm',diacorr=True), "photons")
print("done")