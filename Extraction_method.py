#PhD reseach 2020
#Kittipong Wangnok, D6010218
#School of Physics, Institute of Science, Suranaree University of Technology

#Import all module
import sys
import os
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from statistics import stdev
from statistics import mean
np.seterr(divide='ignore', invalid='ignore')

#Latex font
import matplotlib as mpl
from matplotlib import rc
plt.rc('text', usetex=True)
plt.rc('font', family='serif',size=16)

'''
1. Input file: change 2 input files
'''

#Please change the input file
DP_Leo = open("2013_12_27_dpleo_run040_normal_gaussian.log",'r').readlines()
N_dpleo = len(DP_Leo)

#Read data
MJD_time = []
counts_1 = []
countse_1 = []
counts_2 = []
countse_2 = []
counts_3 = []
countse_3 = []
counts_4 = []
countse_4 = []
counts_5 = []
countse_5 = []

'''
2. Read line of data
Please change the input file: Array starts from 0
'''
##################################################################
for line in open("2013_12_27_dpleo_run040_normal_gaussian.log"):
    li=line.strip()
    if not li.startswith("#"):
        MJD_time.append(float(li.split(" ")[2]))
        counts_1.append(float(li.split(" ")[15]))
        countse_1.append(float(li.split(" ")[16]))
        counts_2.append(float(li.split(" ")[31]))
        countse_2.append(float(li.split(" ")[32]))
        counts_3.append(float(li.split(" ")[47]))
        countse_3.append(float(li.split(" ")[48]))
        counts_4.append(float(li.split(" ")[63]))
        countse_4.append(float(li.split(" ")[64]))
        counts_5.append(float(li.split(" ")[79]))
        countse_5.append(float(li.split(" ")[80]))
##################################################################
########################################################
#Number of data point before reject
print ('Number of data:', N_dpleo)
########################################################

#Input data
x = MJD_time
I_tar = counts_1
I_tar_err = countse_1
I_ref = counts_2
I_ref_err = countse_2
I_chk1 = counts_3
I_chk1_err = countse_3
I_chk2 = counts_4
I_chk2_err = countse_4
I_chk3 = counts_5
I_chk3_err = countse_5



#Print the data#1
print ('---------------------------------------------------------------------------------')
print ('No.             MJD             I_Tar    I_Ref          I_Chk1  I_Chk2  I_Chk3')
print ('---------------------------------------------------------------------------------')
for i in range(len(x)):
        print ('%0.0f\t%0.14f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f' %(i, x[i], I_tar[i], I_ref[i], I_chk1[i], I_chk2[i], I_chk3[i]))

sys.exit
