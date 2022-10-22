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
1. Input file
'''
#################################################################################
#Please change the input file
DP_Leo = open("2013_12_27_dpleo_run040_normal_gaussian_I.log",'r').readlines()
N_dpleo = len(DP_Leo)

#Read data
MJD_time = []
I_counts_1 = []
I_countse_1 = []
I_counts_2 = []
I_countse_2 = []
I_counts_3 = []
I_countse_3 = []
I_counts_4 = []
I_countse_4 = []
I_counts_5 = []
I_countse_5 = []

for line in open("2013_12_27_dpleo_run040_normal_gaussian_I.log"):
    li=line.strip()
    if not li.startswith("#"):
        MJD_time.append(float(li.split(" ")[2]))
        I_counts_1.append(float(li.split(" ")[15]))
        I_countse_1.append(float(li.split(" ")[16]))
        I_counts_2.append(float(li.split(" ")[31]))
        I_countse_2.append(float(li.split(" ")[32]))
        I_counts_3.append(float(li.split(" ")[47]))
        I_countse_3.append(float(li.split(" ")[48]))
        I_counts_4.append(float(li.split(" ")[63]))
        I_countse_4.append(float(li.split(" ")[64]))
        I_counts_5.append(float(li.split(" ")[79]))
        I_countse_5.append(float(li.split(" ")[80]))
#################################################################################
#Number of dpleo data
print ('Number of data I:', N_dpleo)

#Input data
x = MJD_time
I_tar = I_counts_1
I_tar_err = I_countse_1
I_ref = I_counts_2
I_ref_err = I_countse_2
I_chk1 = I_counts_3
I_chk1_err = I_countse_3
I_chk2 = I_counts_4
I_chk2_err = I_countse_4
I_chk3 = I_counts_5
I_chk3_err = I_countse_5
#################################################################################


#Print the data#1
Extraction_method_com1 = []
print ('---------------------------------------------------------------------------------')
print ('No.             MJD             I_Tar    I_Ref          I_Chk1  I_Chk2  I_Chk3')
print ('---------------------------------------------------------------------------------')
for i in range(len(x)):
        print ('%0.0f\t%0.14f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f' %(i, x[i], I_tar[i], I_ref[i], I_chk1[i], I_chk2[i], I_chk3[i]))
        Extraction_method_com1.append('%0.0f\t%0.14f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f' %(i, x[i], I_tar[i], I_ref[i], I_chk1[i], I_chk2[i], I_chk3[i]))

extraction_method = Extraction_method_com1
f = open('Extraction_method_com1.txt', 'w')
#for upper_result in upper_result:
for i in range(len(extraction_method)):
    f.write(str(extraction_method[i])+ '\n')
f.close()

sys.exit
