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
folder = r'C:\Users\z5119993\OneDrive - UNSW\research\JYU LGR\measurements' #for Windows
file_mag = 'dat-short-magn.txt'
file_phase = 'dat-short-phase.txt'
file_freq = 'freqs-antenna2.txt'

file_mag = folder + '/' + file_mag
file_phase = folder + '/' + file_phase
file_freq = folder + '/' + file_freq

with open(file_mag, "r") as my_input_file:
    data_mag = my_input_file.read()
    my_input_file.close()

with open(file_phase, "r") as my_input_file:
    data_phase = my_input_file.read()
    my_input_file.close()

with open(file_freq, "r") as my_input_file:
    data_freq = my_input_file.read()
    my_input_file.close()

mags = data_mag.split(',')
phases = data_phase.split(',')
freqs = data_freq.split(',')
print('conversion successful!')
print(len(mags))
print(len(phases))
print(len(freqs))
#
# # Using library "resonator_tools" for fitting notch type resonators
# port1 = circuit.reflection_port()
#
# port1.add_fromtxt(file_txt, 'dBmagphasedeg', 18, delimiter=' ')
# print('reading of the data is successfully finished')
# #port1.add_fromtxt(file_csv,'linmagphasedeg',3)
#
#
# # port1.autofit(electric_delay=None)
# # # port1.GUIbaselinefit()
# # print('autofit is done')
# # print("Fit results:", port1.fitresults)
# # port1.GUIbaselinefit()
#
# # fit the corrected data
# port1.GUIfit()
# print("Fit results:", port1.fitresults)
# port1.plotall()
#
# # print("single photon limit:",
# #       port1.get_single_photon_limit(diacorr=True), "dBm")
# # print("photons in reso for input -140dBm:",
# #       port1.get_photons_in_resonator(-140, unit='dBm', diacorr=True),
# #       "photons")
#
