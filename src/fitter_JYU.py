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

    plt.plot(x, y, '-r', label='S11', ms=15)
    plt.grid()
    plt.legend()
    plt.ylabel(ylab)
    plt.xlabel(xlab)
    plt.show()
    plt.close()
    # fig.savefig('my_figure.svg')  # vector image



# Data file path
folder  = '/Users/mykhailo/OneDrive - UNSW/research/JYU LGR/measurements' #for Mac
# folder = r'C:\Users\z5119993\OneDrive - UNSW\research\JYU LGR\measurements' #for Windows
file_mag = 'dat-long-magn.txt'
file_phase = 'dat-long-phase.txt'
file_freq = 'freqs-antenna2.txt'


file = folder + '/' + file_mag.replace('.txt', '') + '_COM.txt'
file_mag = folder + '/' + file_mag
file_phase = folder + '/' + file_phase
file_freq = folder + '/' + file_freq



# Read mags. phase. freqs from three different txt files
with open(file_mag, "r") as my_input_file:
    data_mag = my_input_file.read()
    my_input_file.close()

with open(file_phase, "r") as my_input_file:
    data_phase = my_input_file.read()
    my_input_file.close()

with open(file_freq, "r") as my_input_file:
    data_freq = my_input_file.read()
    my_input_file.close()


ms = data_mag.split(',')
mags = []
# mags_dB = []
for m in ms:
    if m!='':
        mags.append(float(m))
        # mags_dB.append(20*np.log10(float(m)))



ps = data_phase.split(',')
phases = []
for p in ps:
    if p!='':
        phases.append(float(p))

fs = data_freq.split(',')
freqs = []
for f in fs:
    if f !='':
        freqs.append(float(f))


print('conversion successful!')

def trim(mags, phases, freqs, fmin, fmax):
    freqs_new = []
    mags_new = []
    phases_new = []

    fmin = fmin * 1e9  # conversion back to [Hz]
    fmax = fmax * 1e9
    for i, f in enumerate(freqs):
        if float(f) > fmin and float(f) < fmax:
            freqs_new.append(f)
            mags_new.append(mags[i])
            phases_new.append(phases[i])

    return mags_new, phases_new, freqs_new

# mags, phases, freqs = trim(mags, phases, freqs, 0, 17)



plot_dataframe(freqs, mags , xlab = "Frequency, Hz", ylab = "S11, dB" )
# Write it the one single file with three columns
exit()

## FITTING


with open(file, "w") as my_out_file:
    my_out_file.write('Frequency ')
    my_out_file.write('Magnitude ')
    my_out_file.write('Phase' + '\n')

    for i in range(len(mags)):
        if mags[i] !='':
            my_out_file.write(str(freqs[i]) + ' ')
            my_out_file.write(str(mags[i]) + ' ')
            my_out_file.write(str(phases[i]) + '\n')

    my_input_file.close()



# Using library "resonator_tools" for fitting notch type resonators
port1 = circuit.reflection_port()
#
port1.add_fromtxt(file, 'dBmagphasedeg', 1, delimiter=' ')
print('reading of the data is successfully finished')

# port1.autofit(electric_delay=None)
port1.GUIbaselinefit()
# print('autofit is done')
# print("Fit results:", port1.fitresults)

# fit the corrected data
port1.GUIfit()
print("Fit results:", port1.fitresults)
port1.plotall()

