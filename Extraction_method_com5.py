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
print ('Number of data: I:', N_dpleo)

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
'''
2. Input file
'''
#################################################################################
#Please change the input file
DP_Leo = open("2013_12_27_dpleo_run040_normal_gaussian_II.log",'r').readlines()
N_dpleo = len(DP_Leo)

#Read data
MJD_time = []
II_counts_1 = []
II_countse_1 = []
II_counts_2 = []
II_countse_2 = []
II_counts_3 = []
II_countse_3 = []
II_counts_4 = []
II_countse_4 = []
II_counts_5 = []
II_countse_5 = []

for line in open("2013_12_27_dpleo_run040_normal_gaussian_II.log"):
    li=line.strip()
    if not li.startswith("#"):
        MJD_time.append(float(li.split(" ")[2]))
        II_counts_1.append(float(li.split(" ")[15]))
        II_countse_1.append(float(li.split(" ")[16]))
        II_counts_2.append(float(li.split(" ")[31]))
        II_countse_2.append(float(li.split(" ")[32]))
        II_counts_3.append(float(li.split(" ")[47]))
        II_countse_3.append(float(li.split(" ")[48]))
        II_counts_4.append(float(li.split(" ")[63]))
        II_countse_4.append(float(li.split(" ")[64]))
        II_counts_5.append(float(li.split(" ")[79]))
        II_countse_5.append(float(li.split(" ")[80]))
#################################################################################
#Number of dpleo data
print ('Number of data II:', N_dpleo)

#Input data
x = MJD_time
II_tar = II_counts_1
II_tar_err = II_countse_1
II_ref = II_counts_2
II_ref_err = II_countse_2
II_chk1 = II_counts_3
II_chk1_err = II_countse_3
II_chk2 = II_counts_4
II_chk2_err = II_countse_4
II_chk3 = II_counts_5
II_chk3_err = II_countse_5
#################################################################################

'''
3. Input file
'''
#################################################################################
#Please change the input file
DP_Leo = open("2013_12_27_dpleo_run040_normal_gaussian_III.log",'r').readlines()
N_dpleo = len(DP_Leo)

#Read data
MJD_time = []
III_counts_1 = []
III_countse_1 = []
III_counts_2 = []
III_countse_2 = []
III_counts_3 = []
III_countse_3 = []
III_counts_4 = []
III_countse_4 = []
III_counts_5 = []
III_countse_5 = []

for line in open("2013_12_27_dpleo_run040_normal_gaussian_III.log"):
    li=line.strip()
    if not li.startswith("#"):
        MJD_time.append(float(li.split(" ")[2]))
        III_counts_1.append(float(li.split(" ")[15]))
        III_countse_1.append(float(li.split(" ")[16]))
        III_counts_2.append(float(li.split(" ")[31]))
        III_countse_2.append(float(li.split(" ")[32]))
        III_counts_3.append(float(li.split(" ")[47]))
        III_countse_3.append(float(li.split(" ")[48]))
        III_counts_4.append(float(li.split(" ")[63]))
        III_countse_4.append(float(li.split(" ")[64]))
        III_counts_5.append(float(li.split(" ")[79]))
        III_countse_5.append(float(li.split(" ")[80]))
#################################################################################
#Number of dpleo data
print ('Number of data III:', N_dpleo)

#Input data
x = MJD_time
III_tar = III_counts_1
III_tar_err = III_countse_1
III_ref = III_counts_2
III_ref_err = III_countse_2
III_chk1 = III_counts_3
III_chk1_err = III_countse_3
III_chk2 = III_counts_4
III_chk2_err = III_countse_4
III_chk3 = III_counts_5
III_chk3_err = III_countse_5
#################################################################################

'''
4. Input file
'''
#################################################################################
#Please change the input file
DP_Leo = open("2013_12_27_dpleo_run040_normal_gaussian_IV.log",'r').readlines()
N_dpleo = len(DP_Leo)

#Read data
MJD_time = []
IV_counts_1 = []
IV_countse_1 = []
IV_counts_2 = []
IV_countse_2 = []
IV_counts_3 = []
IV_countse_3 = []
IV_counts_4 = []
IV_countse_4 = []
IV_counts_5 = []
IV_countse_5 = []

for line in open("2013_12_27_dpleo_run040_normal_gaussian_IV.log"):
    li=line.strip()
    if not li.startswith("#"):
        MJD_time.append(float(li.split(" ")[2]))
        IV_counts_1.append(float(li.split(" ")[15]))
        IV_countse_1.append(float(li.split(" ")[16]))
        IV_counts_2.append(float(li.split(" ")[31]))
        IV_countse_2.append(float(li.split(" ")[32]))
        IV_counts_3.append(float(li.split(" ")[47]))
        IV_countse_3.append(float(li.split(" ")[48]))
        IV_counts_4.append(float(li.split(" ")[63]))
        IV_countse_4.append(float(li.split(" ")[64]))
        IV_counts_5.append(float(li.split(" ")[79]))
        IV_countse_5.append(float(li.split(" ")[80]))
#################################################################################
#Number of dpleo data
print ('Number of data IV:', N_dpleo)

#Input data
x = MJD_time
IV_tar = IV_counts_1
IV_tar_err = IV_countse_1
IV_ref = IV_counts_2
IV_ref_err = IV_countse_2
IV_chk1 = IV_counts_3
IV_chk1_err = IV_countse_3
IV_chk2 = IV_counts_4
IV_chk2_err = IV_countse_4
IV_chk3 = IV_counts_5
IV_chk3_err = IV_countse_5
#################################################################################

'''
5. Input file
'''
#################################################################################
#Please change the input file
DP_Leo = open("2013_12_27_dpleo_run040_normal_gaussian_V.log",'r').readlines()
N_dpleo = len(DP_Leo)

#Read data
MJD_time = []
V_counts_1 = []
V_countse_1 = []
V_counts_2 = []
V_countse_2 = []
V_counts_3 = []
V_countse_3 = []
V_counts_4 = []
V_countse_4 = []
V_counts_5 = []
V_countse_5 = []

for line in open("2013_12_27_dpleo_run040_normal_gaussian_V.log"):
    li=line.strip()
    if not li.startswith("#"):
        MJD_time.append(float(li.split(" ")[2]))
        V_counts_1.append(float(li.split(" ")[15]))
        V_countse_1.append(float(li.split(" ")[16]))
        V_counts_2.append(float(li.split(" ")[31]))
        V_countse_2.append(float(li.split(" ")[32]))
        V_counts_3.append(float(li.split(" ")[47]))
        V_countse_3.append(float(li.split(" ")[48]))
        V_counts_4.append(float(li.split(" ")[63]))
        V_countse_4.append(float(li.split(" ")[64]))
        V_counts_5.append(float(li.split(" ")[79]))
        V_countse_5.append(float(li.split(" ")[80]))
#################################################################################
#Number of dpleo data
print ('Number of data V:', N_dpleo)

#Input data
x = MJD_time
V_tar = V_counts_1
V_tar_err = V_countse_1
V_ref = V_counts_2
V_ref_err = V_countse_2
V_chk1 = V_counts_3
V_chk1_err = V_countse_3
V_chk2 = V_counts_4
V_chk2_err = V_countse_4
V_chk3 = V_counts_5
V_chk3_err = V_countse_5
#################################################################################

#Print the data#1
Extraction_method_com5 = []
print ('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print ('No. \t\t MJD  \t I_Tar \t II_Tar III_Tar IV_Tar \t V_Tar \t I_Ref \t\t II_Ref \t III_Ref \t IV_Ref \t V_Ref          I_Chk1 II_Chk1 III_Chk1 IV_Chk1 V_Chk1 I_Chk2 II_Chk2 III_Chk2 IV_Chk2 V_Chk2 I_Chk3 II_Chk3 III_Chk3 IV_Chk3 V_Chk3')
print ('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
for i in range(len(x)):
        print ('%0.0f\t%0.7f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f'
        %(i, x[i], I_tar[i], II_tar[i], III_tar[i], IV_tar[i], V_tar[i],
        I_ref[i], II_ref[i], III_ref[i], IV_ref[i], V_ref[i],
        I_chk1[i], II_chk1[i], III_chk1[i], IV_chk1[i], V_chk1[i],
        I_chk2[i], II_chk2[i], III_chk2[i], IV_chk2[i], V_chk2[i],
        I_chk3[i], II_chk3[i], III_chk3[i], IV_chk3[i], V_chk3[i]))
        Extraction_method_com5.append('%0.0f\t%0.14f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f\t%0.1f'
        %(i, x[i], I_tar[i], II_tar[i], III_tar[i], IV_tar[i], V_tar[i],
        I_ref[i], II_ref[i], III_ref[i], IV_ref[i], V_ref[i],
        I_chk1[i], II_chk1[i], III_chk1[i], IV_chk1[i], V_chk1[i],
        I_chk2[i], II_chk2[i], III_chk2[i], IV_chk2[i], V_chk2[i],
        I_chk3[i], II_chk3[i], III_chk3[i], IV_chk3[i], V_chk3[i]))

extraction_method = Extraction_method_com5
f = open('Extraction_method_com5.txt', 'w')
#for upper_result in upper_result:
for i in range(len(extraction_method)):
    f.write(str(extraction_method[i])+ '\n')
f.close()

sys.exit

