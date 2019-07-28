
"""
HELMpy, open source package of power flow solvers developed on Python 3 
Copyright (C) 2019 Tulio Molina tuliojose8@gmail.com and Juan José Ortega juanjoseop10@gmail.com

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
"""


# Compare Voltages with MATPOWER .xlsx result file

# Import libraries and functions
import pandas as pd
import numpy as np

pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns',1000)
pd.set_option('display.width',1000)

############   Modify these files names   ###################
data1 = pd.read_excel('put the file name here.xlsx',sheet_name="Buses") #HELMpy file name
data_MATPOWER = pd.read_excel('put the file name here.xlsx',sheet_name='Buses', header=None) #MATPOWER file name

for i in range(len(data_MATPOWER)):
    if(data_MATPOWER[1][i] == 3):
        slack = i
        break


magnitude_1 = data1['Voltages Magnitude']
phase_angles_1 = data1["Voltages Phase Angle"]
magnitude_MATPOWER = data_MATPOWER[7]
phase_angles_MATPOWER = data_MATPOWER[8] - data_MATPOWER[8][slack]

print_all = False ###############################

M = np.zeros(len(magnitude_1))
P_A = np.zeros(len(magnitude_1))

if(print_all):
    print("\n---------1---------")
    for i in range(len(magnitude_1)):
    	print(i,magnitude_1[i],phase_angles_1[i])

    print("\n---------MP---------")
    for i in range(len(magnitude_1)):
    	print(i,magnitude_MATPOWER[i],phase_angles_MATPOWER[i])

if(print_all):
    print("\n----Differences between 1 and MP-----")
for i in range(len(magnitude_1)):
    M[i] = abs(magnitude_1[i]-magnitude_MATPOWER[i])
    P_A[i] = abs(phase_angles_1[i]-phase_angles_MATPOWER[i])
    if(print_all):
        print(i,"Magnitude:",M[i],"Phase Angles:",P_A[i])
        
print("Highest magnitude difference: ",np.max(M))
print("Highest Phase Angles difference: ",np.max(P_A))
