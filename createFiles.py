"""
Creation of files for specific loops, all the numbers are personalized for the parcellation done for PPMI data
Author: Lucia Maria Moya Sans
"""

import numpy as np
import math
import glob
import os
import zipfile
#Creation of the centres dictionaries
with open('tvb\centreslut.txt') as f:
    centres = f.read().splitlines()
count=0
dictionaryCentres = {}
for i in centres:
    dictionaryCentres[i] = count
    count = count + 1
with open('tvb\centreslimbic.txt') as f:
    centresLimbic= f.read().splitlines()
with open('tvb\centresmotor.txt') as f:
    centresMotor = f.read().splitlines()
correctionMatrix = np.loadtxt('tvb\\boolConnectivityMatrix.txt', usecols = range(92))
arrayCentresLimbic = []
arrayCentresMotor = []
for i in centresLimbic:
    arrayCentresLimbic.append(dictionaryCentres[i])
for i in centresMotor:
    arrayCentresMotor.append(dictionaryCentres[i])



directory = "\\tvb"
directory_to = "\\tvb"
os.chdir(directory)
for file in glob.glob("*.zip"):
    pathFile = os.path.join(directory,file)
    with zipfile.ZipFile(pathFile,'r') as zip_ref:
        zip_ref.extractall(directory_to)
    #Extraction of the information and creation of the files
    pathWeights = os.path.join(directory_to, "tvb_inputs\sc.txt")
    pathTracts = os.path.join(directory_to, "tvb_inputs\distance.txt")
    matrixWeights = np.loadtxt(pathWeights, usecols = range(92))
    matrixTracts = np.loadtxt(pathTracts, usecols = range(92))
    newWeightsLimbic = np.zeros((48,48))
    newTractsLimbic = np.zeros((48,48))
    newWeightsmotor = np.zeros((22,22))
    newTractsmotor = np.zeros((22,22))
    countilimbic = 0
    countjlimbic = 0
    countimotor = 0
    countjmotor = 0
    for i in range(92):
        for j in range(92):
            if (i in arrayCentresLimbic) and (j in arrayCentresLimbic):
                newWeightsLimbic[countilimbic][countjlimbic] = matrixWeights[i][j] * correctionMatrix[i][j]
                newTractsLimbic[countilimbic][countjlimbic] = matrixTracts[i][j] * correctionMatrix[i][j]
                countjlimbic = countjlimbic + 1
                if (countjlimbic > 47):
                    countilimbic = countilimbic + 1
                    countjlimbic = 0
            if (i in arrayCentresMotor) and (j in arrayCentresMotor):
                newWeightsmotor[countimotor][countjmotor] = matrixWeights[i][j] * correctionMatrix[i][j]
                newTractsmotor[countimotor][countjmotor] = matrixTracts[i][j] * correctionMatrix[i][j]
                countjmotor = countjmotor + 1
                if (countjmotor > 21):
                    countimotor = countimotor + 1
                    countjmotor = 0
    pathTractsLimbic = 'tvb\\' + file + '\limbic\\tract_lengths.txt'
    pathWeightsLimbic = 'tvb\\' + file + '\limbic\\weights.txt'
    pathTractsMotor = 'tvb\\' + file + '\motor\\tract_lengths_motor.txt'
    pathWeightsMotor = 'tvb\\' + file + '\motor\\weights_motor.txt'

    np.savetxt(pathTractsLimbic,newTractsLimbic)
    np.savetxt(pathWeightsLimbic,newWeightsLimbic)
    np.savetxt(pathTractsMotor,newTractsmotor)
    np.savetxt(pathWeightsMotor,newWeightsmotor)