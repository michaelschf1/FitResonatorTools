'''
Created on 1 Oct. 2018

@author: Mykhailo Savytskyi
@email: m.savytskyi@unsw.edu.au
'''
import csv
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


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


def writeTXT(file, data):
    f = open(file, 'w')
    for line in data:
        if len(line) > 2:
            f.write(str(line[0]) + "\t")
            f.write(str(line[1]) + "\t")
            f.write(str(line[2]) + "\n")
    f.close()
    print('writing to txt file is done')


class NotEnoughInputData(Exception):
    pass


def calibrate_S21dB(data, file_cal):
    data_cal = readCSV(file_cal, headers=7)
    S21dB_cal_func = interpolate_S21dB(data_cal)
    f1, S21dB_1, phDeg_1 = format_S21(data)
    S21dB_calibrated = S21dB_1 - S21dB_cal_func(f1)
    data_calibrated = format_data(f1, S21dB_calibrated, phDeg_1)
#     plot_single(f1, S21dB_calibrated)
    return data_calibrated


def format_data(f, S21, phase):
    data = []
    for i in range(len(f)):
        print(f[i])
        line = str(f[i]) + ' ' + str(S21[i]) + ' ' + str(phase[i]) + '\n'
        data.append(line)
    return data


def interpolate_S21dB(data):
    freq_Hz, S21_dB, phase = format_S21(data)  # @UnusedVariable
    S21_dB_interpol = interp1d(freq_Hz, S21_dB, kind='cubic')
    return S21_dB_interpol


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


def plot_pair(x1, y1, x2, y2):
    plt.plot(x1, y1, 'o', x2, y2, '-')
    plt.legend(['data', 'cubic'], loc='best')
    plt.show()


def plot_single(x1, y1):
    plt.plot(x1, y1, 'o')
    plt.legend(['data'], loc='best')
    plt.show()
