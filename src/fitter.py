'''
Created on 1 Oct. 2018

@author: Mykhailo Savytskyi

@email: m.savytskyi@unsw.edu.au
'''

from resonator_tools import circuit

import utilities as ut

# Data file path
#folder = "C:/Users/z5119993/OneDrive - UNSW/research/measurements/ICE He3/BA3/LGR/@400mK/" # for Windows
folder = '/Users/mykhailo/OneDrive - UNSW/research/measurements/ICE He3/BA3_secondDip_30Apr2019/' # for Mac
file_csv = folder + 'BA3_PBG_400MK_N35PH_MT400_COM.csv'

file_txt = file_csv.replace('csv', 'txt')

ut.convertCSVtoTXT(file_csv, file_txt)

# Using library "resonator_tools" for fitting notch type resonators
port1 = circuit.reflection_port()
port1.add_fromtxt(file_txt, 'dBmagphasedeg', 18, delimiter=' ')
print('reading of the data is successfully finished')

port1.autofit(electric_delay=None)
print('autofit is done')
print("Fit results:", port1.fitresults)
port1.plotall()

port1.GUIfit()

# print("single photon limit:",
#       port1.get_single_photon_limit(diacorr=True), "dBm")
# print("photons in reso for input -140dBm:",
#       port1.get_photons_in_resonator(-140, unit='dBm', diacorr=True),
#       "photons")



# port1=circuit.reflection_port()
# port1.add_froms2p(file_s11, 1,2,'dBmagphasedeg', fdata_unit=1, delimiter=' ')
# port1.autofit( fcrop=(fmin, fmax))
# print("Fit results:", port1.fitresults)
# port1.plotall()
# print("done")
