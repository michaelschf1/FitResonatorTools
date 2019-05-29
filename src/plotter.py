import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fdir = "/Users/mykhailo/OneDrive - UNSW/research/measurements/ICE He3/BA10_tunedLGR_bondWiresReson - Copy/LGR"
regex = "LGR_N5_30DBATT_550MK_V(\d*\.\d*)COM.csv"

freqs, currents, mags = [], [], []
for fname in os.listdir(fdir):
    m = re.match(regex, fname)
    if m is not None:
        fullpath = os.path.join(fdir, m.string)
        current = float(re.split(regex, fname)[1])

        data = pd.read_csv(fullpath, index_col = 0, usecols = [0, 1]) # easiest way to get data out of csv

        freqs += list(data.index)
        mags += list(data['Magnitude, dB'])
        currents += len(data)*[current]

mags = np.array(mags)
colors = (mags - mags.min())/np.ptp(mags) # mags transformed into [0, 1]

# plot in small segments to apply colour gradient
cm = plt.get_cmap("viridis")
plt.scatter(currents, freqs, color = cm(colors), s = 1, marker = 's')
plt.show()
