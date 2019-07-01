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
folder = 'C:/Users/z5119993/OneDrive - UNSW/research/measurements/ICE He3/A9nm_CA1/LGR_tuned_27062019/PBG_Vdc_sweep' #for Windows
# file = 'BA12_PBG_400MK_N40_50DBATTCOM.csv'
# file_csv = folder + '/' + file


regex = "CA1_PBG_n10_60dBAtten_490mK_(\d*\.\d*)V.csv"
# regex = "CA1_PBG_n10_60dBAtten_490mK_(\d*)V.csv"

for fname in os.listdir(folder):
    m = re.match(regex, fname)
    if m is not None:
        voltage = float(re.split(regex, fname)[1])
        file_csv = os.path.join(folder, m.string)

        df = pd.read_csv(file_csv)

        mags = []
        for c in df["S21 complex"]:
            mags.append(complex(c))

        port1 = circuit.reflection_port()
        port1.add_data(df["Frequency, Hz"], mags)

        # df_transposed = df.transpose()
        # df = df_transposed.iloc[1:, ]
        # display(df)
        # port1 = circuit.reflection_port(f_data=df[0].values,
        #                                 z_data_raw=10 ** (df[1].values / 20) * np.exp(
        #                                     1j * df[2].values / 180 * np.pi))

        # fit the corected data
        port1.GUIfit()
        df_results = pd.DataFrame([port1.fitresults])
        df_results['VoltageDC, V'] = voltage
        display(df_results)
        ut.append_df_to_excel(
            'C:/Users/z5119993/OneDrive - UNSW/research/measurements/ICE He3/A9nm_CA1/RESULTS/PBG_CA1_S2_Vdc_FITS.xlsx',
            df_results)

