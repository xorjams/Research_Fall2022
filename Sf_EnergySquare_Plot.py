# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:30:31 2022

@author: 15083
"""

import numpy as np
import os
import matplotlib.pyplot as plt
from numpy import diff
#from Sf_DataPlot import dEdt

os.chdir('C:\\Users\\15083\\Documents\\NEU_semester_2\\Feiguin_Group_Research_Spring_2022\\Code\\Oct_17')

filenames =  os.listdir('C:\\Users\\15083\\Documents\\NEU_semester_2\\Feiguin_Group_Research_Spring_2022\\Code\\Oct_17')

def read_col1(fname, col=0, convert=float, sep=None):

    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]
     
        
     
def read_col2(fname, col = 1, convert = float, sep=None):
    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]
     
        

Data1 = np.loadtxt("McData_July")  
sfTemp =  Data1[:,0]
Beta = 1/sfTemp
BetaSquare = 1/sfTemp**2
sfEnergySquare =  Data1[:,3]
sfEnergy = Data1[:,1]
                                                                        
DataCombine = np.column_stack((sfTemp, sfEnergySquare))
#DataCombine2 = np.column_stack((sfTemp, sfEnergy))

DataCombineSort =  DataCombine[np.argsort(DataCombine[:, 0])]
#DataCombineSort2 = DataCombine[np.argsort(DataCombine2[:, 0])]

sfTemp = DataCombineSort[:,0]
sfEnergySquare = DataCombineSort[:,1]

#sfEnergy = DataCombineSort2[:,1]


sfHeatCap = BetaSquare*(sfEnergySquare - np.square(sfEnergy))



sfEnergySquare -= 45
#sfTemp.sort()
#sfEnergy.sort()



sfTempSD = np.std(sfTemp)
sfHeatCapSD = np.std(sfEnergySquare)

sfTempError = sfTempSD/np.sqrt(1000)

sfEnergyError = sfEnergySquare/np.sqrt(1000)
fig, ax = plt.subplots()
ax.set_ylabel("EnergySquare")
ax.set_xlabel("Temperature")







os.chdir('C:\\Users\\15083\\Documents\\NEU_semester_2\\Feiguin_Group_Research_Spring_2022\\Code')

Data = np.loadtxt("L_20_datatest.txt")  


Temp = Data[:,0]
#HeatCap = Data[:,1]
Energy = Data[:,3]
EnergySquare = Data[:,13]

HeatCap = Data[:,1]

sfTempcorrect = Temp
sfHeatCapcorrect = HeatCap
sfEnergySquarecorrect = EnergySquare

TempError = np.std(Temp)/np.sqrt(1000)
HeatCapError = np.std(sfHeatCap)/np.sqrt(1000)
EnergySquareError = np.std(EnergySquare)/np.sqrt(1000)


plt.errorbar(sfTempcorrect, sfEnergySquarecorrect, yerr = EnergySquareError, marker = ".", label = "3D_XY")

plt.errorbar(sfTemp, sfEnergySquare, yerr = EnergySquareError, xerr = None , marker = ".", label = "SpinFermion correct")

plt.legend(["SpinFermionCorrect", "SpinFermion_Trial"] )




#plt.plot(sfTemp, dEdt, marker = '.')

plt.xscale("log")
plt.show()