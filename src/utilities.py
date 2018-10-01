'''
Created on 1 Oct. 2018

@author: Mykhailo Savytskyi
@email: m.savytskyi@unsw.edu.au
'''
import csv
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


# cut the data according to set frequency range
def trim(data, fmin, fmax):
    data_new = []
    fmin = fmin * 1e9  # conversion back to [Hz]
    fmax = fmax * 1e9
    for line in data:
        if len(line) > 2 and float(line[0]) > fmin and float(line[0]) < fmax:
            data_new.append(line)

    if not data_new:
        raise NotEnoughInputData('range is too narrow, list is empty!')
    return data_new


# read a csv file to buffer
def readCSV(file, headers=7):
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        data = []
        for i in range(headers):  # @UnusedVariable
            next(reader)

        for row in reader:
            data.append(row)

    print('reading of CSV file is done')
    return data


# write to txt file formatted data
def writeTXT(file, data):
    f = open(file, 'w')
    for line in data:
        if len(line) > 2:
            line = line.split(" ")
            f.write(str(line[0]) + ' ')
            f.write(str(line[1]) + ' ')
            f.write(str(line[2]) + '\n')
    f.close()
    print('writing to txt file is done')


# exception when the frequency range is chosen outside the available data
class NotEnoughInputData(Exception):
    pass


# do calibaration for dB magnitude S21
def calibrate_S21dB(data, file_cal):
    data_cal = readCSV(file_cal, headers=7)
    S21dB_cal_func = interpolate_S21dB(data_cal)
    f1, S21dB_1, phDeg_1 = format_S21(data)
    S21dB_calibrated = S21dB_1 - S21dB_cal_func(f1)
    data_calibrated = format_data(f1, S21dB_calibrated, phDeg_1)
#     plot_single(f1, S21dB_calibrated)
    return data_calibrated


# form one data array from three lists
def format_data(f, S21, phase):
    data = []
    for i in range(len(f)):
        line = str(f[i]) + ' ' + str(S21[i]) + ' ' + str(phase[i]) + '\n'
        data.append(line)
    return data


# interpolation of calibration points for its further implementation
def interpolate_S21dB(data):
    freq_Hz, S21_dB, phase = format_S21(data)  # @UnusedVariable
    S21_dB_interpol = interp1d(freq_Hz, S21_dB, kind='cubic')
    return S21_dB_interpol


# form three lists form one array
def format_S21(data):
    freq_Hz = []
    S21_dB = []
    phDeg = []
    for line in data:
        if len(line) > 2:
            freq_Hz.append(float(line[0]))
            S21_dB.append(float(line[1]))
            phDeg.append(float(line[2]))
    return freq_Hz, S21_dB, phDeg


# plot two data lists
def plot_pair(x1, y1, x2, y2):
    plt.plot(x1, y1, 'o', x2, y2, '-')
    plt.legend(['data', 'cubic'], loc='best')
    plt.show()


# plot one data list
def plot_single(x1, y1):
    plt.plot(x1, y1, 'o')
    plt.legend(['data'], loc='best')
    plt.show()
