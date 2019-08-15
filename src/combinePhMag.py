import utilities_pack as ut
from resonator_tools import circuit


folder = r'C:\Users\z5119993\OneDrive - UNSW\research\measurements\ICE He3\BA3_secondDip_30Apr2019\dc voltage' #for Windows
#folder  = '/Users/mykhailo/OneDrive - UNSW/research/measurements/ICE He3/BA10_tunedLGR_bondWiresReson - Copy/LGR' #for Mac


pairs = ut.matchMagPhasePairs(folder)
ut.combineAll(folder, pairs)

comFiles = ut.findFiles(folder, 'COM.csv')
print('COM:')
print(comFiles)


