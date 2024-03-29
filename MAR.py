# developed by Yanhui Yang  Feb 15 2021

import sys
import numpy as np
from mar_funs import *
import glob

# kpc  km/s  Msun 


flist = sorted(glob.glob("./part*.asc")) 
flist_time = sorted(glob.glob("./gpa*.txt"))
n_in = len(flist)
print("List of input files: %s" % flist)
print("Number of input files: %d.\n" % n_in)

M_R_list = []
time_list = get_time(flist_time)

i = 0
while(i < n_in):
    print("Reading %s." % flist[i])
    pos_list, mass_list = get_part(flist[i])
    if i == 0:
        M_tot = np.sum(mass_list)
        R = 1e-5  # R = 0.01 pc = 1e-5 kpc
        # M_R = internal_M(R)
        print("%d particles." % len(mass_list))
        print("Total mass: %.5e Msun" % M_tot)
        print("Accretion radius: %.5e kpc" % R)
    x = get_x(pos_list) #temp
    COM = mass_center(pos_list, mass_list)
    M_R = internal_M(pos_list, mass_list, R)
    M_R_list.append(M_R)
    print("x_min = %f" % min(x)) #temp
    print("x_max = %f" % max(x)) #temp
    print("Center of mass: %s kpc" % COM)
    print("Internal mass: %.5e Msun.\n" % M_R)
    i = i + 1

print("Internal mass list: %s Msun.\n" % M_R_list)

AR_list, TR_list = get_acc_rate(M_R_list, time_list)
print("Accrretion rate list: %s" % AR_list)

# write_rate
write_AR(AR_list, TR_list, "accretion_rates.txt")









