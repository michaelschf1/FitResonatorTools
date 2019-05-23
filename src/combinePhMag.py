import utilities as ut
from resonator_tools import circuit


#folder = 'C:/Users/z5119993/OneDrive - UNSW/research/measurements/ICE He3/BA10_tuned_LGR - Copy' #for Windows
folder  = '/Users/mykhailo/OneDrive - UNSW/research/measurements/ICE He3/BA10 - Copy/PBG/magnetic field' #for Mac


pairs = ut.matchMagPhasePairs(folder)
ut.combineAll(folder, pairs)

comFiles = ut.findFiles(folder, 'COM.csv')
print('COM:')
print(comFiles)


