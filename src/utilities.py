'''
Created on 1 Oct. 2018

@author: Mykhailo Savytskyi
@email: m.savytskyi@unsw.edu.au
'''
import csv


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
