'''

@author: Mykhailo Savytskyi

@email: m.savytskyi@unsw.edu.au
'''

from resonator_tools import circuit

import FitResonatorTools.src.utilities as ut
import pandas as pd
import numpy as np
from IPython.display import display
import re, os


# Data file path
#folder  = '/Users/mykhailo/OneDrive - UNSW/research/measurements/ICE He3/BA11' #for Mac
folder = 'C:/Users/z5119993/OneDrive - UNSW/research/measurements/ICE He3/BA11_bondWiresReson/PBG/500mK/voltage' #for Windows
file = 'BA11_PBG_500mK_n10_V17.csv'
file_csv = folder + '/' + file


df = pd.read_csv(file_csv)
df_transposed = df.transpose()
df=df_transposed.iloc[1:,]


port1 = circuit.reflection_port(f_data=df[0].values,
                                z_data_raw=10 ** (df[1].values / 20) * np.exp(
                                    1j * df[2].values / 180 * np.pi))
#fit and remove the base line
#port1.GUIbaselinefit()

# fit the corected data
port1.GUIfit()
df_results = pd.DataFrame([port1.fitresults])
df_results['Voltage, V'] = 17
display(df_results)

save = input('Do you want to save these results?')
if save == 'y':
    ut.append_df_to_excel(
        'C:/Users/z5119993/OneDrive - UNSW/research/measurements/ICE He3/BA11_bondWiresReson/BA11_PBG_voltage_FITS.xlsx',
        df_results)

#print('Single photon limit: {0} dBm'.format(port1.get_single_photon_limit()))
