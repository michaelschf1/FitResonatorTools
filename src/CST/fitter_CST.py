'''
Created on 1 Oct. 2018

@author: Mykhailo Savytskyi

@email: m.savytskyi@unsw.edu.au
'''

from resonator_tools import circuit
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import FitResonatorTools.src.utilities as ut
import pandas as pd

def plot_dataframe(x, y , xlab = "Frequency, Hz", ylab = "S11 lin" ):

    matplotlib.rcParams.update({'font.size': 20})
    fig = plt.figure()

    plt.plot(x, y, '-or', label='S11', ms=3)
    plt.grid()
    plt.legend()
    plt.ylabel(ylab)
    plt.xlabel(xlab)
    plt.show()
    plt.close()
    # fig.savefig('my_figure.svg')  # vector image



# Data file path
folder  = '/Users/mykhailo/OneDrive - UNSW/research/CST/LGR&PBG_new' #for Mac
# folder = r'C:\Users\z5119993\OneDrive - UNSW\research\JYU LGR\measurements' #for Windows
file = 'CA5_flipchipLossless_full.txt'

file_new = folder + '/' + file.replace('.txt', '') + '_COM.txt'
file = folder + '/' + file


# Read mags. phase. freqs from three different txt files
freqs = []
mags = []
phi = []
with open(file, "r") as my_input_file:
    i = 0
    for line in my_input_file:
        if i>2:
            data = line.split('\t')
            freqs.append(float(data[0]))
            mags.append(float(data[1]))
            phi.append(float(data[2]))
        else:
            i+=1

    my_input_file.close()



# mags = []
# mags_dB = []
# for m in ms:
#     if m!='':
#         mags.append(float(m))
#         # mags_dB.append(20*np.log10(float(m)))
#


print('conversion successful!')

def trim(mags, phases, freqs, fmin, fmax):
    freqs_new = []
    mags_new = []
    phases_new = []

    fmin = fmin  # conversion back to [Hz]
    fmax = fmax
    for i, f in enumerate(freqs):
        if float(f) > fmin and float(f) < fmax:
            freqs_new.append(f)
            mags_new.append(mags[i])
            phases_new.append(phases[i])

    return mags_new, phases_new, freqs_new

mags, phi, freqs = trim(mags, phi, freqs, 6.86, 6.89)



plot_dataframe(freqs, mags, xlab = "Frequency, GHz", ylab = "S11, mag" )
plot_dataframe(freqs, phi, xlab = "Frequency, GHz", ylab = "S11, deg" )
# Write it the one single file with three columns
# exit()

## FITTING


with open(file_new, "w") as my_out_file:
    my_out_file.write('Frequency ')
    my_out_file.write('Magnitude ')
    my_out_file.write('Phase' + '\n')

    for i in range(len(mags)):
        if mags[i] !='':
            my_out_file.write(str(freqs[i]) + ' ')
            my_out_file.write(str(mags[i]) + ' ')
            my_out_file.write(str(phi[i]) + '\n')

    my_input_file.close()



# Using library "resonator_tools" for fitting notch type resonators
port1 = circuit.reflection_port()
#
port1.add_fromtxt(file_new, 'linmagphasedeg', 1, delimiter=' ')
print('reading of the data is successfully finished')

# port1.autofit(electric_delay=None)
# port1.GUIbaselinefit()
# print('autofit is done')
# print("Fit results:", port1.fitresults)

# fit the corrected data
port1.GUIfit()
print("Fit results:", port1.fitresults)
port1.plotall()

