'''
Created on 1 Oct. 2018

@author: Mykhailo Savytskyi

@email: m.savytskyi@unsw.edu.au
'''

from resonator_tools import circuit
from utilities import readCSV, trim, calibrate_S21dB, writeTXT

# Data file path
folder = ("/Users/mykhailo/OneDrive - UNSW/research/measurements/" +
          "Sample PBG AA1/LGR_PBG_28Aug18_1.4K_meas_NoCal/")
file_s21 = folder + 'SMA1-3_peak7.8_noDC_n20.csv'

# Calibration file path
folder_cal = ("/Users/mykhailo/OneDrive - UNSW/research/measurements/" +
              "Sample PBG AA1/LGR_PBG_25Aug18_calibration_1.4K/")
file_cal = folder_cal + 'S21_SMA1t0SMA2_1p4K_0dBm.csv'

# Frequency range that will be analyzed
fmin = 7.83  # frequency in [GHz]
fmax = 7.88  # frequency in [GHz]

# Reading csv file
data = readCSV(file_s21, headers=7)
# Cut according to the chosen frequency range
data = trim(data, fmin, fmax)
# Add calibration if needed
data = calibrate_S21dB(data, file_cal)
# Writing the data to txt file for further fitting
writeTXT('S21.txt', data)

# Using library "resonator_tools" for fitting notch type resonators
port1 = circuit.notch_port()
port1.add_fromtxt('S21.txt', 'dBmagphasedeg', 1)
print('reading of the data is successfully finished')

port1.autofit(electric_delay=None)
print('autofit is done')
print("Fit results:", port1.fitresults)
port1.plotall()

# port1.GUIfit()
# print("Fit results:", port1.fitresults)
# port1.plotall()
# print("single photon limit:",
#       port1.get_single_photon_limit(diacorr=True), "dBm")
# print("photons in reso for input -140dBm:",
#       port1.get_photons_in_resonator(-140, unit='dBm', diacorr=True),
#       "photons")
print("done")
