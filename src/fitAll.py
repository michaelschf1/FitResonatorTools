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
folder = r'C:\Users\z5119993\OneDrive - UNSW\research\measurements\ICE He3\BA13 Si28-Bi17\S2_removedBndWires\PBG_Vdc_sweep' #for Windows
# file = 'BA12_PBG_400MK_N40_50DBATTCOM.csv'
# file_csv = folder + '/' + file


regex = "BA13_PBG_S3_540mK_n20_(\d*\.\d*)V.csv"
# regex = "CA1_PBG_n10_60dBAtten_490mK_(\d*)V.csv"
count=0
for fname in os.listdir(folder):
    m = re.match(regex, fname)
    if m is not None:
        voltage = float(re.split(regex, fname)[1])
        file_csv = os.path.join(folder, m.string)

        df = pd.read_csv(file_csv)

        # mags = []
        # phs = []
        # comp = []
        # for m in df["Magnitude, dB"]:
        #     mags.append(m)
        # for p in df["Phase, deg"]:
        #     phs.append(p)
        #
        # for i,m in enumerate(mags):
        #     s21_complex = 10 ** (mags[i] / 20) * np.exp(1j * phs[i] * np.pi / 180)
        #     comp.append(s21_complex)


        comp = []
        for c in df["S21 complex"]:
            comp.append(complex(c))

        port1 = circuit.reflection_port()
        port1.add_data(df["Frequency, Hz"], comp)

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
        # display(df_results)
        if count==0:
            ut.append_df_to_excel(
                r'C:\Users\z5119993\OneDrive - UNSW\research\measurements\ICE He3\BA13 Si28-Bi17\S2_removedBndWires\PBG_Vdc_sweep\PBG_BA13_S3_Vdc_FITS.xlsx',
                df_results, header_custom=True)
            count=+1
        else:
            ut.append_df_to_excel(
                r'C:\Users\z5119993\OneDrive - UNSW\research\measurements\ICE He3\BA13 Si28-Bi17\S2_removedBndWires\PBG_Vdc_sweep\PBG_BA13_S3_Vdc_FITS.xlsx',
                df_results, header_custom=False)

