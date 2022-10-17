



import numpy as np
import os

os.chdir('C:\\Users\\15083\\Documents\\NEU_semester_2\\Feiguin_Group_Research_Spring_2022\\Code\\Oct_17')

filenames =  os.listdir('C:\\Users\\15083\\Documents\\NEU_semester_2\\Feiguin_Group_Research_Spring_2022\\Code\\Oct_17')
'''
def read_col(fname, col=0, convert=float, sep=None):

    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]

def read_col2(fname, col=1, convert=float, sep=None):

    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]
   
def read_col3(fname, col=2, convert=float, sep=None):

    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]


def read_col4(fname, col=3, convert=float, sep=None):

    with open(fname) as fobj:
         return [convert(line.split(sep=sep)[col]) for line in fobj]

'''

filenameslen = len(filenames)
f = open("McData_July", "w")
for i in range(filenameslen):
    Data = np.genfromtxt(filenames[i])
    currentname = filenames[i]
    currentnameparts = currentname.split('_')
    Temp = currentnameparts[2]
    Temp = float(Temp)
    
    res = Data[:,0]
    res2 = Data[:,1]
    res3 = Data[:,2]
    res4 = Data[:,3]
    
    EnergyArray = np.asarray(res)
    HeatCapacityArray = np.asarray(res2)
    #EnergySquareArray = np.asarray(res3)
    #StaggMagArray = np.asarray(res4)
    
    
    Beta = 1/Temp
    AvgEnergy = np.average(EnergyArray)
    #HeatCapacity = np.average(HeatCapacityArray)
    AvgEnergySquare = np.average(HeatCapacityArray)
    HeatCapacityArray -= AvgEnergy**2
    #HeatCapacity = (Beta**2)*np.average(HeatCapacityArray)
    HeatCapacity= (Beta**2)*np.average(HeatCapacityArray)

    #AvgStaggMag = np.average(StaggMagArray)
    AvgEnergy = round(AvgEnergy, 6)
    
    AvgHeatCap = np.average(HeatCapacityArray)/(Temp*Temp)
    
    #AvgHeatCap = (AvgEnergySquare - AvgEnergy**2)/(Temp**2)
    Temp = round(Temp, 6)
    
    print(str(AvgEnergy))
    print(Temp)
    

    f.write('{:<12}  {:<12}  {:<12} {:<12}'.format(Temp, AvgEnergy,  HeatCapacity, AvgEnergySquare))
    f.write("\n")
    
            
            
f.close()