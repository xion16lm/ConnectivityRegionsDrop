import numpy as np
import math
matrixWeights = np.loadtxt('tvb\weights.txt', usecols = range(92))
matrixTracts = np.loadtxt('tvb\\tract_lengths.txt', usecols = range(92))
with open('tvb\centreslut.txt') as f:
    centres = f.read().splitlines()
count=0
dictionaryCentres = {}
for i in centres:
    dictionaryCentres[i] = count
    count = count + 1
with open('tvb\centreslimbic.txt') as f:
    centresMotor = f.read().splitlines()
count=0
arrayCentresMotor = []
for i in centresMotor:
    arrayCentresMotor.append(dictionaryCentres[i])
newWeights = np.zeros((48,48))
newTracts = np.zeros((48,48))
counti = 0
countj = 0
for i in range(92):
    for j in range(92):
        if (i in arrayCentresMotor) and (j in arrayCentresMotor):
            newWeights[counti][countj] = matrixWeights[i][j]
            newTracts[counti][countj] = matrixTracts[i][j]
            countj = countj + 1
            if (countj > 47):
                counti = counti + 1
                countj = 0
np.savetxt('tvb\\tract_lengths_limbic.txt',newTracts)
np.savetxt('tvb\weights_limbic.txt',newWeights)